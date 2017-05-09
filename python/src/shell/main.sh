export HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

rm -rf screen/* 2>/dev/null


spark-submit    --executor-cores    4       \
                --executor-memory   5G      \
                --num-executors     10      \
                --master            yarn    \
                --conf spark.default.parallelism=1000   \
                --conf spark.storage.memoryFraction=0.5 \
                --conf spark.shuffle.memoryFraction=0.4 \
                main.py  1>screen/screen 2>screen/error

if [ $? -eq 0 ];then
    echo -e "任务正常执行" >> screen/screen
else
    echo -e "任务执行失败" >> screen/screen
fi

