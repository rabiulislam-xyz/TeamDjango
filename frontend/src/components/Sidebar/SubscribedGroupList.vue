<template>
    <div >
        <v-card v-for="group in groups"
                class="mt-1" 
                ripple
                hover
                :to="'/dashboard/group/'+group.slug"
                :key="group.slug">

          <div class="ml-2" @click="onGroup(group.slug)">
            <h5>{{ group.name }}</h5>
            <small>{{ group.members_count }} members</small>
          </div>
       
        </v-card>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        groups: this.$store.getters.subscribedGroups
      }
    },
    methods: {
      onGroup (groupSlug){
        let this_alias = this
        axios.get("http://127.0.0.1:8000/group/"+groupSlug, {
          headers: { "Authorization": "JWT " + this_alias.$store.getters.token}
        })
        .then(function (response) {
          this_alias.$store.dispatch('setGroupMessages', response.data.messages)
        })
        .catch(function (error) {
          console.log(error)
        })
      }
    }
  }
</script>