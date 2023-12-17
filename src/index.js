// Allow getting the token
require('dotenv').config();

// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits, Activity, Presence, ActivityType } = require('discord.js');
/**
 * @type {string}
 */
const token = process.env.DISCORD_TOKEN;

const prefix = "?";

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds]});

// When the client is ready, run this code (only once).
// The distinction between `client: Client<boolean>` and `readyClient: Client<true>` is important for TypeScript developers.
// It makes some properties non-nullable.
client.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
    client.channels.fetch("1138112432624124056").then(function(value) {
        value.send("discord.js is functioning");
    });
});

client.once(Events.MessageCreate, message => {
    if (message.content.startsWith(`${prefix}hi`)) {
        message.reply(`Hi, ${message.author.displayName}!`);
    }

    if (message.content == client.user.tag) {
        message.reply("Beep boop! I'm keeping the server cool!");
    }

    if (message.content.startsWith(`${prefix}offline`)) {
        message.reply("Going offline");
        client.destroy();
    }
});

// Log in to Discord with your client's token
client.login(token);