#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from sparse_matrix import SparseMatrix
from pyspark import SparkConf,SparkContext


def test_read_data_from_local(_sc):
    data_list    = []
    content_list = file("../../data/multiply.txt").read().split("\n")[0:-1]
    for line in content_list:
        data_list.append(line.split("\t"))
    return _sc.parallelize(data_list,4)
        

def test_multiply(_sc,_obj_sparse):
    debug = True
    if debug:
        print "enter test_multiply"
    data_rdd = test_read_data_from_local(_sc)
    data_rdd.take(3)
    left_matrix     = data_rdd
    right_matrix    = data_rdd.map(lambda x:[x[1],x[0],x[2]])
    print "left_matrix::",left_matrix.collect()
    print "right_matrix::",right_matrix.collect()
    

def test_cosine_simi(sc,_obj_sparse):
    debug = True
    if debug:
        print "enter test_cosine_simi"

def test_slpa(sc,_obj_sparse):
    debug = True
    if debug:
        print "enter test_slpa"

def test_pagerank(sc,_obj_sparse):
    debug = True
    if debug:
        print "enter test_pagerank"


if __name__ == '__main__':
    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ##    加载类SparseMatrix
    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    obj_sparse = SparseMatrix()

    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ##    spark设置
    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    APP_NAME = "sparse"
    conf = SparkConf().setAppName(APP_NAME)
    sc = SparkContext(conf=conf)

    test_multiply(sc,obj_sparse)        ## 测试矩阵乘法
    test_cosine_simi(sc,obj_sparse)     ## 测试余弦距离
    test_slpa(sc,obj_sparse)            ## 测试slpa算法
    test_pagerank(sc,obj_sparse)        ## 测试pagerank算法



    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ##    程序执行结束,清理现场
    ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    sc.stop()
    print "<<\twork finish"
    sys.exit(0)

