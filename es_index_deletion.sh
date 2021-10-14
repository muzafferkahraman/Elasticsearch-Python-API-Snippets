DAYSTOKEEP=30

indiceid=($(curl '127.0.0.1:9200/_cat/indices?pretty' | grep nuage_ | awk '{print $3}'))
today=`date +"%Y-%m-%d"`
deletethisandbefore=`date +"%Y-%m-%d" -d "-$DAYSTOKEEP days"`
echo
echo
echo
echo "Today is "$today
echo
echo "This Script will delete all indeces of date " $deletethisandbefore  " and before!"
echo
echo
echo
i=0
for s in ${indiceid[@]}; do
 day=${s: -10}
 if [[ $day  < $deletethisandbefore ]] ||  [[ $day == $deletethisandbefore ]]; then
    python vsd_elasticctl.py delete_index ${indiceid[i]}
    wait
    echo  "Date: "$day" Index name: "${indiceid[i]} "deletion finished"
 fi
((i=i+1))
done


