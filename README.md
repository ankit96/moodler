# moodler
--------------
Moodler the bot is here to avoid anymore overdue submissions for you 
![img](https://raw.githubusercontent.com/ankit96/moodler/master/demo.gif)



## Usage
###You can go through this [`post`](https://medium.com/@ankit15/moodler-4138a99e045c#.2ae9tsh81)
##### /moodle
- from any slack channel just type `/moodle [username],[password],[batch]`. All your comming submission deadlines would be displayed.
- eg : /moodle ankituser,ankitpass,D<br />
      here,<br />
      username=ankituser<br />
      password=ankitpass<br />
      batch = D
      

##### /setmoodle
- from any channel type `/setmoodle [username],[password],[batch]`.Your data will get stored in
our  database and automatic daily reminders will be posted in this channel.
- eg : /setmoodle ankituser,ankitpass,D<br />
      here,<br />
      username=ankituser<br />
      password=ankitpass<br />
      batch = D<br />
- Note: password is being encrypted before inserting into database


##### /deletemoodle
- from any channel type `/deletemoodle `.Your data will get removed from
our  database .
- eg : /deletemoodle<br />


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
       - Usage Hint: `[username][password][batch]`.
   3. For deleting your login data from moodlers tb
   
       - Command: `/deletemoodle`
       - URL: `https://spitmoodler.herokuapp.com/deletemoodle`
       - method: `POST`
       - For the **Autocomplete help text**, check to show the command in autocomplete list.
       - Description: `deletes your login data.`
       - Usage Hint: 
       

## Contributing
- Please use the [issue tracker](https://github.com/ankit96/moodler/issues) to report any bugs or file feature requests.

## LICENCE

- [MIT LICENSE](https://github.com/ankit96/moodler/blob/master/LICENSE) (c) Ankit Sagwekar
