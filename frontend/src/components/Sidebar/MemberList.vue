<template>
    <div >

    <v-list one-line>
          <v-list-tile  @click=""
                        v-for="member in members"
                        ripple
                        hover
                        :to="'/dashboard/member/'+ member.id"
                        :key="member.id">
            <v-list-tile-action>
                <v-avatar size="36px" slot="activator">
                  <img :src="member.photo" alt="">
                </v-avatar>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ member.username }}</v-list-tile-title>
              <v-list-tile-sub-title>{{ member.email }}</v-list-tile-sub-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-icon color="green darken-3">fiber_manual_record</v-icon>
            </v-list-tile-action>
            <v-divider></v-divider>
          </v-list-tile>
      </v-list>
    </div>
</template>

<script>
  export default {
    data () {
      return {
        
      }
    },
    computed: {
      members () {
        return this.$store.getters.allMembers
      }
    },
    methods: {
      onMember (memberId){
        console.log('go to member ' + memberId)
      }
    }
  }
</script>