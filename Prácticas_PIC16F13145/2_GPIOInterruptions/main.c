#include "mcc_generated_files/system/system.h"

/*
    Acá se configuró el Pin RC2 (LED) como output y el RC3 (SWITCH) como input con 
    weak pull up e interrupción negativa
*/


void Switch_Interrupt() {
    LED_Toggle();
}

int main(void)
{
    SYSTEM_Initialize();

    // Enable the Global Interrupts 
    INTERRUPT_GlobalInterruptEnable();

    // Enable the Peripheral Interrupts 
    INTERRUPT_PeripheralInterruptEnable();

    SWITCH_SetInterruptHandler(*Switch_Interrupt);

    while(1)
    {
    }    
}