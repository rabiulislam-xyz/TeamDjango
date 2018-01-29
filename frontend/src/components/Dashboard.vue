<template>
    <div>
        <v-container fluid grid-list-md>
            <v-layout row wrap>
                <v-flex xs3>
                    <left-sidebar></left-sidebar>
                </v-flex>
                <v-flex xs6>
                    <router-view></router-view>
                </v-flex>
                <v-flex xs3>
                    <right-sidebar></right-sidebar>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>


<script>
    import LeftSidebar from './Sidebar/LeftSidebar'
    import RightSidebar from './Sidebar/RightSidebar'

    export default {
        name: 'dashboard',
        data () {
            return {
                name: 'rabiul islam '
            }
        },
        computed: {
            userIsAuthenticated: function(){
                return this.$store.getters.userIsAuthenticated
            }
        },
        components: {
            LeftSidebar,
            RightSidebar
        }
    }
</script>