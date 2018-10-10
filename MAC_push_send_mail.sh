#!/bin/bash
git add *
git commit -m "${1}"
git push origin master
read -p "send email?(y/n)" check
mail_list=""
for email in `cat mail_list`
do
    mail_list=${mail_list},${email}
done
mail_list=${mail_list#,}
if [ $check == "y" ]; then
    osascript ~/.myscript/send.scpt "${1}" "${mail_list}"
fi
