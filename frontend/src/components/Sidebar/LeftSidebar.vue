<template>
    <div>
      <profile></profile>
      <SubscribedGroupList></SubscribedGroupList>
    </div>   
</template>

<script>
  import Profile from './Profile'
  import SubscribedGroupList from './SubscribedGroupList'

  export default {
    name: 'left-sidebar',
    // data () {
    //   return {

    //   }
    // },
    components: {
            Profile,
            SubscribedGroupList
        }

  }
</script>