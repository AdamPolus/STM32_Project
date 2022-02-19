/*
 * common.c
 *
 *  Created on: Feb 19, 2022
 *      Author: apolus
 */
#include "common.h"
#include <math.h>
#include "arm_math.h"
#include "math_helper.h"

float32_t LINEAR_TRANSFORM(float32_t x, float32_t amin,float32_t amax, float32_t bmin, float32_t bmax){
	if(x>=amin && x<=amax){
	return (((x-amin)/(amax-amin))*(bmax-bmin)+bmin);
	}
	if(x>amax){
		return bmax;
	}
	if(x<amin){
		return bmin;
	}
}
