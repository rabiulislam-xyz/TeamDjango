<template>
    <div>

        <MessageInput @newMessageText="newMessageText">
        </MessageInput>

        <!-- <v-text-field box 
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
        </p> -->

        <v-card v-for="message in messages" 
                :key="message.id"
                class="mb-1">
            <v-card-title >
                <div>
                    <b>{{ message.sender }}</b><br>
                    <small class="grey--text">{{message.timestamp}}</small><br>
                    <span>{{ message.content }}</span>
                </div>
            </v-card-title>
            <v-card-actions>
                <v-btn icon><v-icon>favorite_border</v-icon></v-btn>
                <v-btn icon><v-icon>comment</v-icon></v-btn>
                <v-spacer></v-spacer>

                <v-menu bottom offset-y>
                    <v-btn slot="activator" icon>
                        <v-btn icon>
                            <v-icon>more_horiz</v-icon>
                        </v-btn>
                    </v-btn>
                    <v-list>
                      <v-list-tile v-for="(item, i) in moreButton" :key="i" @click="">
                        <v-list-tile-title>{{ item }}</v-list-tile-title>
                      </v-list-tile>
                    </v-list>
                </v-menu>

            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
    import MessageInput from './MessageInput'
    export default {
        name: 'messages',
        data () {
            return {
                user: null,
                messages: [],
                newMessageText: '',
                moreButton: ['report','hide']
            }
        },
        methods: {
            onLike () {
                ''
            },
            onNewMessageText (messageText) {
                this.messages.unshift({sender: this.user,
                                    content: messageText,
                                    timestamp: new Date()
                                })
                this.newMessageText = ''
            }
        },
        mounted () {
            this.messages = this.messages.concat(this.$store.getters.messages)
            this.user = this.$store.getters.user
        },
        components: {
            MessageInput
        }
    }
</script>