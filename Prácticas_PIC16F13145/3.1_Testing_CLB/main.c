#include "mcc_generated_files/system/system.h"

/*
    Esta práctica la hice por mi cuenta

    Extraje esta implementación de https://www.youtube.com/watch?v=tlamrtNFeJQ para probar el clb
    
    Más información en:

    https://www.cnx-software.com/2024/02/08/microchip-introduces-pic16f13145-series-mcus-with-customizable-logic/
    https://www.reddit.com/r/FPGA/comments/1amp7gu/microchip_introduces_pic16f13145_series_mcus_with/
    https://forum.digikey.com/t/using-the-configurable-logic-block-clb-for-rising-and-falling-edge-detection/53140
    https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/peripherals/system-flexibility/clb
*/

int main(void)
{
    SYSTEM_Initialize();

    while(1)
    {
        for (uint8_t i = 0; i < 10; i++) {
            CLB1_SWIN_Write8(i);
            __delay_ms(500);
        }
    }    
}