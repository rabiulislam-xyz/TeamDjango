<template>
    <div>
        <v-text-field box 
                      multi-line
                      label="send your think..."
                      color="primary"
                      v-model="newMessageText">
                    
        </v-text-field>
        
        <p class="text-xs-right">
            <v-btn v-if="newMessageText.length > 0"
                    @click="onSend">
                <v-icon color="primary">send</v-icon>
            </v-btn>
        </p>
    </div>
</template>

<script>
    export default {
        name: 'messageInput',
        props: ['user'],
        data () {
            return {
                newMessageText: ''
            }
        },
        methods: {
            onSend () {
                this.$emit('newMessageText', this.newMessageText)
                // this.messages.unshift({sender: this.user.username,
                //                     content: this.newMessageText,
                //                     timestamp: new Date()
                //                 })
                this.newMessageText = ''
            }
        }
    }
</script>