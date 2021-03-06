#!/bin/bash
project=("/Users/originals/Boostnote" "/Users/originals/.myscript" "/Users/originals/blog/public")
function update() {
    for pro in ${project[@]}; do
        cd $pro
        echo -e "\n==============update ${pro}"
        count=`git status -s | wc -l`
        if [ $count -gt 0 ]; then
            echo -e ">>>>>>>>>>>>>>something in buffer\n"
            git add *
            git commit -m "update"
            if [ $? -eq 0 ]; then
                git push origin master
            else
                echo untrack file
                git status
            fi
        fi
    done
}
update
