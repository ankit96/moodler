# moodler
--------------
Moodler the bot is here to avoid anymore overdue submissions for you 
![img](https://raw.githubusercontent.com/ankit96/moodler/master/demo.gif)



## Usage

##### /moodle
- from any slack channel just type `/moodle [username][password][batch]`. All your comming submission deadlines would be displayed.
- eg : /moodle ankituser,ankitpass,D<br />
      here,<br />
      username=ankituser<br />
      password=ankitpass<br />
      batch = D
      

##### /setmoodle
- from a private channel in which you are the only member type `/setmoodle [username][password][batch][channel name]`.Your data will get stored in
our  database and automatic daily reminders will be posted in this channel.
- eg : /setmoodle ankituser,ankitpass,D,#moodle<br />
      here,<br />
      username=ankituser<br />
      password=ankitpass<br />
      batch = D<br />
      private channel name= #moodle<br />
- Note: #moodle is the private channel which i created for myself and no other member is present except me
- Likewise you need to create your own private channel 


## Integrate it with your team


1. Go to your channel
2. Goto `https://[team_name].slack.com/apps/manage/custom-integrations	`.
3. Click on **Add** next to **Slash Commands**.


   1. For usage as shown in above gif image
   
       - Command: `/moodle`
       - URL: `https://spitmoodler.herokuapp.com/moodle`
       - method: `POST`
       - For the **Autocomplete help text**, check to show the command in autocomplete list.
       - Description: `gives  future submission deadlines.`
       - Usage Hint: `[username][password][batch]`.
       
   2. For storing your data[username,password,batch,channel] in our database **[optional]**
   
       - Command: `/setmoodle`
       - URL: `https://spitmoodler.herokuapp.com/setmoodle`
       - method: `POST`
       - For the **Autocomplete help text**, check to show the command in autocomplete list.
       - Description: `Saves your data for automatic reminders.`
       - Usage Hint: `[username][password][batch][channel]`.


##Note: /spitmoodle command

- It is not mandatory,but integrating this command would allow you to store your login data with us.All those
 users who will provide us with  their login data will recieve automatic reminders everyday about 
 their future submission deadlines.
 
- Also after integrating /spitmoodle command ,users are adviced to use this command only once in a seperate **Private** channel which they 
need to create for moodle reminders only.Everyday reminders will be posted on that specific channel.


## Contributing
- Please use the [issue tracker](https://github.com/ankit96/moodler/issues) to report any bugs or file feature requests.

## LICENCE

- [MIT LICENSE](https://github.com/ankit96/moodler/blob/master/LICENSE) (c) Ankit Sagwekar