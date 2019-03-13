#include <math.h>
#include "mtx.h"

/*
 * Function: mtx_create
 * ------------------------
 *  Construct mtx_matrix from data input
 *
 *  Result: mtx_matrix mtx_out
 */

void mtx_create(int32_t rows, int32_t cols, float *data, struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;

    if (rows <= MAX_ROWS)  mtx_out->rows = rows;
    else mtx_out->rows = MAX_ROWS;

    if (cols <= MAX_COLS)  mtx_out->cols = cols; 
    else mtx_out->cols = MAX_COLS;
    
    for (row=1;row <= rows;row++){
        for (col=1;col <= cols;col++){
            mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = 
                data[(row-1)*mtx_out->cols + (col-1)];
        }
    }
    return;
}

/*
 * Function: mtx_create_ones
 * ------------------------
 *  Construct mtx_matrix of ones
 *
 *  Result: mtx_matrix mtx_out
 */

void mtx_create_ones(int32_t rows, int32_t cols, struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;
   
    if (rows <= MAX_ROWS)  mtx_out->rows = rows;
    else mtx_out->rows = MAX_ROWS;

    if (cols <= MAX_COLS)  mtx_out->cols = cols; 
    else mtx_out->cols = MAX_COLS;
    
    for (row=1;row <= rows;row++){
        for (col=1;col <= cols;col++){
            mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = 1.0;
        }
    }
    return;
}

/*
 * Function: mtx_create_eye
 * ------------------------
 *  Construct Identity matrix
 *
 *  Result: mtx_matrix mtx_out
 */

void mtx_create_eye(int32_t rows, int32_t cols, struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;
   
    if (rows <= MAX_ROWS)  mtx_out->rows = rows;
    else mtx_out->rows = MAX_ROWS;

    if (cols <= MAX_COLS)  mtx_out->cols = cols; 
    else mtx_out->cols = MAX_COLS;

    if (rows != cols) rows = cols;
    
    for (row=1;row <= rows;row++){
        for (col=1;col <= cols;col++){
            if (row == col)
            mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = 1.0;
            else 
            mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = 0.0;
        }
    }
    return;
}

/*
 * Function: mtx_create_val
 * ------------------------
 *  Construct mtx_matrix of value
 *
 *  Result: mtx_matrix mtx_out
 */

void mtx_create_val(int32_t rows, int32_t cols, 
                        struct mtx_matrix* mtx_out, float val){
    int32_t row;
    int32_t col;
   
    if (rows <= MAX_ROWS)  mtx_out->rows = rows;
    else mtx_out->rows = MAX_ROWS;

    if (cols <= MAX_COLS)  mtx_out->cols = cols; 
    else mtx_out->cols = MAX_COLS;
    
    for (row=1;row <= rows;row++){
        for (col=1;col <= cols;col++){
            mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = val; 
        }
    }
    return;
}
/*
 * Function: mtx_get
 * ------------------------
 * Get value from mtx_matrix
 *
 * Result: float from i,j
 *
 */

float mtx_get(int32_t row, int32_t col, struct mtx_matrix* mtx_a){
    if (row<=mtx_a->rows && col<=mtx_a->cols){
        return mtx_a->data[(row-1)*mtx_a->cols + (col-1)];    
    } else {
        return -1.0;
    }
}

/*
 * Function: mtx_set
 * ------------------------
 * Set value in mtx_matrix
 *
 */

void mtx_set(int32_t row, int32_t col, struct mtx_matrix* mtx_out, float data){
    if (row<=mtx_out->rows && col<=mtx_out->cols){
        mtx_out->data[(row-1)*mtx_out->cols + (col-1)] = data;
    }
}

/*
 * Function: mtx_sum
 * ------------------------
 *  Add two matrices
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_sum(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_b, 
                struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;
    float data;

    if ((mtx_a->rows != mtx_b->rows) || (mtx_a->cols != mtx_b->cols) || 
        (mtx_out->rows != mtx_b->rows) || (mtx_out->cols != mtx_b->cols)) {
        return -1;
    }

    for (row=1;row <= mtx_a->rows;row++){
        for (col=1;col <= mtx_a->cols;col++){
            data = mtx_get(row,col,mtx_a) + mtx_get(row,col,mtx_b);
            mtx_set(row,col,mtx_out,data);    
        }
    }
    return 0;
}

/*
 * Function: mtx_scaler
 * ------------------------
 *  Multiply matrix elements by scaler
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_scale(struct mtx_matrix* mtx_a, float scaler, 
                struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;
    float data;

    if ((mtx_out->rows != mtx_a->rows) || (mtx_out->cols != mtx_a->cols)) {
        return -1;
    }

    for (row=1;row <= mtx_a->rows;row++){
        for (col=1;col <= mtx_a->cols;col++){
            data = scaler*mtx_get(row,col,mtx_a);
            mtx_set(row,col,mtx_out,data);    
        }
    }
    return 0;
}

/*
 * Function: mtx_mult
 * ------------------------
 *  Multiply two matrices
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_mult(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_b, 
                struct mtx_matrix* mtx_out){
    int32_t row_a;
    int32_t row_b;
    int32_t col_b;
    float data;

    if ((mtx_a->cols != mtx_b->rows) || 
        (mtx_out->rows != mtx_a->rows) || (mtx_out->cols != mtx_b->cols)) {
        return -1;
    }

    for (row_a=1;row_a <= mtx_a->rows;row_a++){
        for (col_b=1;col_b <= mtx_b->cols;col_b++){
            data = 0;
            for (row_b=1;row_b <= mtx_b->rows;row_b++){
                data = data + 
                        mtx_get(row_a,row_b,mtx_a)*mtx_get(row_b, col_b,mtx_b);
            }
            mtx_set(row_a,col_b,mtx_out,data);    
        }
    }
    return 0;
}

/*
 * Function: mtx_trans
 * ------------------------
 *  Transpose Matrix
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_trans(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;
    float data;

    if ((mtx_out->rows != mtx_a->cols) || (mtx_out->cols != mtx_a->rows)){
        return -1;
    }

    for (row=1;row <= mtx_a->rows;row++){
        for (col=1;col <= mtx_a->cols;col++){
            data = mtx_get(row,col,mtx_a);
            mtx_set(col,row,mtx_out,data);    
        }
    }
    return 0;
}


/*
 * Function: mtx_det
 * ------------------------
 *  Determinant of Matrix
 *
 *  Result: float 
 */

float mtx_det(struct mtx_matrix* mtx_a){
    float det;

    det = 0;
    if ((mtx_a->rows != mtx_a->cols)) {
        return 0;
    }
    
    /*Fixed Determinant Calculation - reduce matrix allocation*/
    if (mtx_a->rows == 1){
        det = mtx_get(1,1,mtx_a);
    } else if (mtx_a->rows == 2){
        det = mtx_get(1,1,mtx_a)*mtx_get(2,2,mtx_a)
                -mtx_get(1,2,mtx_a)*mtx_get(2,1,mtx_a);
    } else if (mtx_a->rows == 3) {
        det = mtx_get(1,1,mtx_a)
                * (mtx_get(2,2,mtx_a)*mtx_get(3,3,mtx_a)
                    -mtx_get(2,3,mtx_a)*mtx_get(3,2,mtx_a))
              - mtx_get(1,2,mtx_a)
                * (mtx_get(2,1,mtx_a)*mtx_get(3,3,mtx_a)
                    -mtx_get(2,3,mtx_a)*mtx_get(3,1,mtx_a))
              + mtx_get(1,3,mtx_a)
                * (mtx_get(2,1,mtx_a)*mtx_get(3,2,mtx_a)
                    -mtx_get(2,2,mtx_a)*mtx_get(3,1,mtx_a));
    } else if (mtx_a->rows == 4) {
        det = mtx_get(1,1,mtx_a)
                    * (mtx_get(2,2,mtx_a)
                        * (mtx_get(3,3,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,3,mtx_a))
                    - mtx_get(2,3,mtx_a)
                        * (mtx_get(3,2,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,2,mtx_a))
                    + mtx_get(2,4,mtx_a)
                        * (mtx_get(3,2,mtx_a)*mtx_get(4,3,mtx_a)
                            -mtx_get(3,3,mtx_a)*mtx_get(4,2,mtx_a)))
               - mtx_get(1,2,mtx_a)
                    * (mtx_get(2,1,mtx_a)
                        * (mtx_get(3,3,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,3,mtx_a))
                    - mtx_get(2,3,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,1,mtx_a))
                    + mtx_get(2,4,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,3,mtx_a)
                            -mtx_get(3,3,mtx_a)*mtx_get(4,1,mtx_a)))
                + mtx_get(1,3,mtx_a)
                    * (mtx_get(2,1,mtx_a)
                        * (mtx_get(3,2,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,2,mtx_a))
                    - mtx_get(2,2,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,4,mtx_a)
                            -mtx_get(3,4,mtx_a)*mtx_get(4,1,mtx_a))
                    + mtx_get(2,4,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,2,mtx_a)
                            -mtx_get(3,2,mtx_a)*mtx_get(4,1,mtx_a)))
                - mtx_get(1,4,mtx_a)
                    * (mtx_get(2,1,mtx_a)
                        * (mtx_get(3,2,mtx_a)*mtx_get(4,3,mtx_a)
                            -mtx_get(3,3,mtx_a)*mtx_get(4,2,mtx_a))
                    - mtx_get(2,2,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,3,mtx_a)
                            -mtx_get(3,3,mtx_a)*mtx_get(4,1,mtx_a))
                    + mtx_get(2,3,mtx_a)
                        * (mtx_get(3,1,mtx_a)*mtx_get(4,2,mtx_a)
                            -mtx_get(3,2,mtx_a)*mtx_get(4,1,mtx_a)));
    }
    return det;
}

/*
 * Function: mtx_norm
 * ------------------------
 *  L2,1-norm of matrix
 *
 *  Result: float
 */

float mtx_norm(struct mtx_matrix* mtx_a){
    int32_t row;
    int32_t col;
    float norm;

    norm = 0;
    for (row=1;row <= mtx_a->rows;row++){
        for (col=1;col <= mtx_a->cols;col++){
            norm += mtx_get(row,col,mtx_a)*mtx_get(row,col,mtx_a);
        }
    }
    norm = sqrtf(norm);
    return norm;
}

/*
 * Function: mtx_inv
 * ------------------------
 *  Inverse Matrix, max size 3x3
 *  larger matrices return error
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_inv(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out){
    float scale;
    float det;

    det = mtx_det(mtx_a);

    if ((mtx_out->rows != mtx_a->rows) || (mtx_out->cols != mtx_a->cols) ||
        (mtx_a->rows != mtx_a->cols) || mtx_a->rows > 3) {
        /*Return -1 if Matrix is non-square*/
        return -1;
    } else if (det == 0.0) {
        /*Return -2 if Matrix is singular*/
        return -2;
    }

    scale = 1.0f/det;

    if (mtx_a->rows == 1) {
        mtx_set(1,1,mtx_out,scale);    
    }else if (mtx_a->rows == 2){
        mtx_set(1,1,mtx_out,    
            scale*(mtx_get(2,2,mtx_a)));
        mtx_set(1,2,mtx_out,    
            scale*(-1*(mtx_get(1,2,mtx_a))));
        mtx_set(2,1,mtx_out,    
            scale*(-1*(mtx_get(2,1,mtx_a))));
        mtx_set(2,2,mtx_out,    
            scale*(mtx_get(1,1,mtx_a)));
    }else if (mtx_a->rows == 3) {
        mtx_set(1,1,mtx_out,    
            scale*(mtx_get(2,2,mtx_a)*mtx_get(3,3,mtx_a)
                -mtx_get(2,3,mtx_a)*mtx_get(3,2,mtx_a)));
        mtx_set(1,2,mtx_out,    
            scale*(-1*(mtx_get(1,2,mtx_a)*mtx_get(3,3,mtx_a)
                -mtx_get(1,3,mtx_a)*mtx_get(3,2,mtx_a))));
        mtx_set(1,3,mtx_out,    
            scale*(mtx_get(1,2,mtx_a)*mtx_get(2,3,mtx_a)
                -mtx_get(1,3,mtx_a)*mtx_get(2,2,mtx_a)));
        mtx_set(2,1,mtx_out,    
            scale*(-1*(mtx_get(2,1,mtx_a)*mtx_get(3,3,mtx_a)
                -mtx_get(2,3,mtx_a)*mtx_get(3,1,mtx_a))));
        mtx_set(2,2,mtx_out,    
            scale*(mtx_get(1,1,mtx_a)*mtx_get(3,3,mtx_a)
                -mtx_get(1,3,mtx_a)*mtx_get(3,1,mtx_a)));
        mtx_set(2,3,mtx_out,    
            scale*(-1*(mtx_get(1,1,mtx_a)*mtx_get(2,3,mtx_a)
                -mtx_get(1,3,mtx_a)*mtx_get(2,1,mtx_a))));
        mtx_set(3,1,mtx_out,    
            scale*(mtx_get(2,1,mtx_a)*mtx_get(3,2,mtx_a)
                -mtx_get(2,2,mtx_a)*mtx_get(3,1,mtx_a)));
        mtx_set(3,2,mtx_out,    
            scale*(-1*(mtx_get(1,1,mtx_a)*mtx_get(3,2,mtx_a)
                -mtx_get(1,2,mtx_a)*mtx_get(3,1,mtx_a))));
        mtx_set(3,3,mtx_out,    
            scale*(mtx_get(1,1,mtx_a)*mtx_get(2,2,mtx_a)
                -mtx_get(1,2,mtx_a)*mtx_get(2,1,mtx_a)));
    }
    return 0;
}

/*
 * Function: mtx_max
 * ------------------------
 * Get maximum value from mtx_matrix
 *
 * Result: float 
 *
 */

float mtx_max(struct mtx_matrix* mtx_a, int32_t* loc_row, int32_t* loc_col){
    int32_t row;
    int32_t col;
    float max;
    float ele;

    max = mtx_get(1,1,mtx_a);
    for (row=1;row<=mtx_a->rows;row++){
        for (col=1;col<=mtx_a->cols;col++){
            ele = mtx_get(row,col,mtx_a);
            if (ele >= max){  
                max = ele;
                *loc_row = row;
                *loc_col = col;
            }
        }
    }
    return max;
}

/*
 * Function: mtx_trace
 * ------------------------
 * Calculate trace of matrix
 *
 * Result: float 
 *
 */

float mtx_trace(struct mtx_matrix* mtx_a){
    int32_t row;
    float trace;

    trace = 0;
    if (mtx_a->rows == mtx_a->cols) {
        for (row=1;row<=mtx_a->rows;row++){
            trace += mtx_get(row,row,mtx_a);
        }
    }
    return trace;
}

/*
 * Function: mtx_ss
 * ------------------------
 *  Return skew symmetric matrix
 *  Input must be 3 vector
 *
 *  Result: mtx_matrix
 */

int32_t mtx_ss(struct mtx_matrix* vec, struct mtx_matrix* mtx_out){

    if(vec->rows != 3 || vec->cols !=1){
        return -1;
    }

    mtx_set(1,1,mtx_out,    0);
    mtx_set(1,2,mtx_out,    -1*mtx_get(3,1,vec));
    mtx_set(1,3,mtx_out,    mtx_get(2,1,vec));
    mtx_set(2,1,mtx_out,    mtx_get(3,1,vec));
    mtx_set(2,2,mtx_out,    0);
    mtx_set(2,3,mtx_out,    -1*mtx_get(1,1,vec));
    mtx_set(3,1,mtx_out,    -1*mtx_get(2,1,vec));
    mtx_set(3,2,mtx_out,    mtx_get(1,1,vec));
    mtx_set(3,3,mtx_out,    0);

    return 0;
}

/*
 * Function: mtx_copy
 * ------------------------
 *  Copy first matrix to second
 *
 *  Result: mtx_matrix mtx_out
 */

int32_t mtx_copy(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out){
    int32_t row;
    int32_t col;

    if ( (mtx_out->rows != mtx_a->rows) || (mtx_out->cols != mtx_a->cols)) {
        return -1;
    }

    for (row=1;row <= mtx_a->rows;row++){
        for (col=1;col <= mtx_a->cols;col++){
            mtx_set(row,col,mtx_out,    mtx_get(row,col,mtx_a));    
        }
    }
    return 0;
}
