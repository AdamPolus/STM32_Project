/*
 * LCD1602.h
 *
 *  Created on: 24-Jan-2021
 *      Author: AP
 */

#ifndef INC_LCD1602_
#define INC_LCD1602_
#include <string.h>
#include <stdio.h>

void Lcd_init (void);   // initialize lcd

void lcd_send_cmd (char cmd);  // send command to the lcd

void lcd_send_data (char data);  // send data to the lcd

void Lcd_send_string (char *str);  // send string to the lcd

void Lcd_put_cur(int row, int col);  // put cursor at the entered position row (0 or 1), col (0-15);

void Lcd_clear (void);


#endif /* INC_LCD1602_ */
