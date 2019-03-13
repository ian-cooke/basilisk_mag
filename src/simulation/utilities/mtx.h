/* ***********************************************************************
 * file:    mtx.h
 * author:	? Header didn't exist (Andre L Antunes de Sa edit)
 * created on:	?
 *
 * Matrix math wrapper
 *
 * ***********************************************************************
 */

#ifndef __MTX_H
#define __MTX_H

#include "types.h"

#define MAX_ROWS 14
#define MAX_COLS 14

struct mtx_matrix{
    int32_t rows;
    int32_t cols;
    float data[MAX_ROWS*MAX_COLS];
};

void mtx_create(int32_t rows, int32_t cols, float *data, struct mtx_matrix* mtx_out);
void mtx_create_ones(int32_t rows, int32_t cols, struct mtx_matrix* mtx_out);
void mtx_create_eye(int32_t rows, int32_t cols, struct mtx_matrix* mtx_out);
void mtx_create_val(int32_t rows, int32_t cols, struct mtx_matrix* mtx_out, float val);
float mtx_get(int32_t row, int32_t col, struct mtx_matrix* mtx_a);
void mtx_set(int32_t row, int32_t col, struct mtx_matrix* mtx_out, float data);
int32_t mtx_sum(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_b, struct mtx_matrix* mtx_out);
int32_t mtx_scale(struct mtx_matrix* mtx_a, float scaler, struct mtx_matrix* mtx_out);
int32_t mtx_mult(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_b, struct mtx_matrix* mtx_out);
int32_t mtx_trans(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out);
float mtx_det(struct mtx_matrix* mtx_a);
float mtx_norm(struct mtx_matrix* mtx_a);
int32_t mtx_inv(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out);
float mtx_max(struct mtx_matrix* mtx_a, int32_t* loc_row, int32_t* loc_col);
float mtx_trace(struct mtx_matrix* mtx_a);
int32_t mtx_ss(struct mtx_matrix* vec, struct mtx_matrix* mtx_out);
int32_t mtx_copy(struct mtx_matrix* mtx_a, struct mtx_matrix* mtx_out);

#endif
