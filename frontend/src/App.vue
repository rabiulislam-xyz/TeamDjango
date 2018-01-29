<template>
  <v-app>
       
    <v-navigation-drawer temporary absolute v-model="sideNav">
      <v-list>

        <v-list-tile v-for="item in menuItems" :key="item.title">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-btn flat @click="item.action">{{ item.title }}</v-btn>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile v-if="userIsAuthenticated">
          <v-list-tile-action>
            <v-icon>exit_to_app</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-btn flat>Logout</v-btn>
          </v-list-tile-content>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>

    <v-toolbar dark class="primary">
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          Team Django
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-side-icon 
        class="hidden-sm-and-up"
        @click.stop="sideNav = !sideNav"></v-toolbar-side-icon>
      <v-toolbar-items class="hidden-xs-only">

        <v-btn flat 
               v-for="item in menuItems" 
               :key="item.title"
               @click="item.action">
          <v-icon left>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
        <v-btn
          v-if="userIsAuthenticated"
          flat
          @click="onLogout">
          <v-icon left>exit_to_app</v-icon>
          Logout
        </v-btn>

      </v-toolbar-items>
    </v-toolbar>
    
       <v-layout row justify-center>
          <v-dialog v-model="loginDialog" max-width="320">
            <v-card>
              <v-card-text>
                <v-form v-model="valid">
                  <v-text-field
                    label="Username"
                    v-model="username"
                    required
                  ></v-text-field>
                  <v-text-field
                    type="password"
                    label="Password"
                    v-model="password"
                    required
                  ></v-text-field>
                  <v-spacer></v-spacer>
                  <v-btn @click.prevent="onSubmitLogin">submit</v-btn>
                  <v-btn @click="loginDialog = !loginDialog">cancel</v-btn>
                </v-form>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-layout>

   
      <router-view></router-view>

  </v-app>
</template>


<script >
import axios from 'axios'

export default {
  data() {
    return {
      sideNav: false,
      loginDialog: false,
      username: '',
      password: '',
      valid: false
    }
  },
  computed: {
    menuItems() {
      let menuItems = [
        { icon: 'lock_open', title: 'Login', action: this.onLogin }
      ]
      if (this.userIsAuthenticated) {
        menuItems = [
          { icon: 'search', title: 'Search', action: this.onSearch },
          { icon: 'people', title: 'Create Group', action: this.onCreateGroup }
        ]
      }
      return menuItems
    },
    userIsAuthenticated() {
      return this.$store.getters.user !== null && this.$store.getters.user !== undefined
    }
  },
  methods: {
    onLogin() {
      this.loginDialog = !this.loginDialog
    },
    onSubmitLogin() {
      if (this.loginFormIsValid()) {
        let this_alias = this
        axios.post("http://127.0.0.1:8000/api-token-auth/", {
            username: this.username,
            password: this.password
          }, { "Content-Type": "application/html"})
          .then(function(response) {
            // save retireaved token
            var token = response.data.token
            this_alias.$store.dispatch('setToken', token)

            // retrieve profile object of current user
            axios.get("http://127.0.0.1:8000/account/profile/", {
                headers: { "Authorization": "JWT " + token }
            })
            .then(function(response){
                // set current user data to local cache
                // and logg the user in
                this_alias.$store.dispatch('login', response.data.user)
                // set subscribed groups
                this_alias.$store.dispatch('setSubscribedGroups', response.data.user.subscribed_groups)
                // retrieve all members
                this_alias.$store.dispatch('setAllMembers', response.data.members)
                // close login dialog
                this_alias.loginDialog = !this_alias.loginDialog
                // redirect to dashboard
                this_alias.$router.push('/dashboard')
            })
            .catch(function(error) {
                console.log(error)
            })

          })
          .catch(function(error) {
            console.log(error);
          });
      }


    },
    loginFormIsValid() {
      if (this.username && this.password) {
        return true
      } else {
        return false
      }
    },
    onSearch() {
      console.log('search button clicked')
    },
    onCreateGroup() {
      console.log('create group')
    },
    onLogout() {
      this.$store.dispatch('logout')
      this.$router.push('/')
    }
  }
} 
</script>
