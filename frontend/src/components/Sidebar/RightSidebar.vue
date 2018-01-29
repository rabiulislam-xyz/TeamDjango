<template>
    <div>
      <member-list></member-list>
    </div>   
</template>

<script>
  import MemberList from './MemberList'

  export default {
    name: 'right-sidebar',
    components: {
            MemberList
        }
  }
</script>