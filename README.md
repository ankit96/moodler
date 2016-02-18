# Moodler
It will sign in on behalf of you on moodle and will give you deadline for every subject experiments which you have enrolled
![stack Overflow](https://raw.githubusercontent.com/ankit96/moodler/master/demo.gif)

# Usage
from any slack channel just type /moodle [username,password,batch].Moodler will provide you will your todays moodle submission deadlines.

#Integrate it with your team
You can form your class group on slack and integrate /moodle in it.

#Instructions for integrating in your slack channel
1. Go to your channel
2. Click on Configure Integrations.
3. Scroll all the way down to DIY Integrations & Customizations section.
4. Click on Add next to Slash Commands.
  1. Command: moodle
  2. URL: https://spitmoodler.herokuapp.com/moodle
  3.  method: POST.
  4. For the Autocomplete help text, check to show the command in autocomplete list.
  5. Description: Moodler will signin for you and will give your  todays moodle submission deadlines.
  6. Usage Hint: [search query].
  7. Descriptiive Level: Search Query.
      
#Contributing
Please use the [issue tracker](https://github.com/ankit96/moodler/issues) to report any bugs or file feature requests.

#License
[MIT LICENSE](https://github.com/ankit96/moodler/blob/master/LICENSE) (c) Ankit Sagwekar
