<template>
    <v-container>
        
      <v-carousel>
        <v-carousel-item v-for="(item,i) in items" 
                        v-bind:src="item.src" 
                        :key="i"></v-carousel-item>
        </v-carousel>

        <div v-if="userIsAuthenticated" class="text-xs-center mt-3">
            <v-btn large
                   round
                   color="primary"
                   to="/dashboard">Go Dashboard
            </v-btn>
        </div>

        <div v-else class="text-xs-center mt-3">
            <v-btn large
                   round
                   color="primary"
                   @click.native.stop="registerDialog = true">
              Register Now
            </v-btn>
        </div>

        <v-layout row justify-center>
          <v-dialog v-model="registerDialog" max-width="290">
            <v-card>
              <v-card-title class="headline">
                Registration currently not allowed!
              </v-card-title>
              <v-card-text>for joining on team django you have to registration on django course. next batch is comming soon. be waiting...</v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" flat="flat" @click.native="registerDialog = false">close</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-layout>

    </v-container>
</template>


<script>
  export default {
    data () {
      return {
        registerDialog: false,
        items: [
          {
            src: 'https://vuetifyjs.com/static/doc-images/carousel/squirrel.jpg'
          },
          {
            src: 'https://vuetifyjs.com/static/doc-images/carousel/sky.jpg'
          },
          {
            src: 'https://vuetifyjs.com/static/doc-images/carousel/bird.jpg'
          },
          {
            src: 'https://vuetifyjs.com/static/doc-images/carousel/planet.jpg'
          }
        ]
      }
    },
    computed: {
      userIsAuthenticated () {
        return this.$store.getters.user !== null && this.$store.getters.user !== undefined
      }
    }
  }
</script>