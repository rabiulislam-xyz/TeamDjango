<template>

  <v-card>
    <v-card-media :src="photo" height="200px">
      <v-layout column class="media">
        <v-card-title>
          <v-btn dark
                 outline 
                 icon
                 @click="onEditProfile">
            <v-icon>edit</v-icon>
          </v-btn>
        </v-card-title>
      </v-layout>
    </v-card-media>
      
    <v-card-title primary-title>
      <div>
        <small>{{username}}</small>
        <h3 class="headline mb-0">{{ fullname }}</h3>
        <div>{{ email }}</div>
        <div>
          <a :href="website" 
              style="text-decoration:none;color: black;">
            {{ website }}
          </a>
        </div>
      </div>
    </v-card-title>
       
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        username: '',
        fullname: '',
        email: '',
        website: '',
        photo: ''
      }
    },
    methods: {
      onEditProfile () {
        console.log('clicked on edit profile')
      }
    },
    mounted () {
      let user = this.$store.getters.user
      this.username = user.username
      this.fullname = user.first_name +' '+user.last_name
      this.email = user.email
      this.website = user.website
      this.photo = user.photo
    }
  }
</script>