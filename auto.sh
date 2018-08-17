#!/bin/bash
project=("/Users/originals/Boostnote" "/Users/originals/.myscript")
function update() {
    for pro in ${project[@]}; do
        cd $pro
        echo update $pro
        count=`git status -s | wc -l`
        if [ $count -gt 0 ]; then
            echo "something in buffer"
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
