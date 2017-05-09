# sparse_matrix
Sparse Matrix operation on spark （矩阵以coo格式存储）
举例：
  矩阵为[1,2,3;
          2,3,4]
  coo存储：
    1,1,1
    1,2,2
    1,3,3
    2,1,2
    2,2,3
    2,3,4


# python/src/sparse_matrix.py:
  SparseMatrix.multiply            ## 稀疏矩阵乘法  
  SparseMatrix.transpose           ## 矩阵转置    
  SparseMatrix.add                 ## 矩阵加法    
  SparseMatrix.sub                 ## 矩阵减法      
  SparseMatrix.cosine_simi         ## 稀疏矩阵计算余弦距离    
  SparseMatrix.extract_tfidf       ## 稀疏矩阵提取tfidf特征    
  SparseMatrix.convert2csr         ## 矩阵由coo格式转为csr格式   
  SparseMatrix.middle              ## 计算coo矩阵值的中位数   
