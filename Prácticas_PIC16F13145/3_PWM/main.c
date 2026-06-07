 /*
    Usamos el Timer0 y PWM1, also el RC3 como input switch y RC2 como output LED 
    (que son el botón y el led que vienen en la placa de desarrollo)

    Recordatorio: PWM1 se activa iniciando el Timer2
*/

#include "mcc_generated_files/system/system.h"

void Timer_Callback() {
    LED_Toggle(); 
}

uint16_t duty_cycle = 1000; 

void set_pwm_duty_cycle() {
    // hice un switch para mayor estilo y placer
    switch (duty_cycle) {
        case 1000:
            duty_cycle = 100;
        default:
            duty_cycle += 10;
    }
    PWM1_LoadDutyValue(duty_cycle);
}

int main(void)
{
    SYSTEM_Initialize();

    // Enable the Global Interrupts 
    INTERRUPT_GlobalInterruptEnable(); 

    // Enable the Peripheral Interrupts 
    INTERRUPT_PeripheralInterruptEnable();

    // Estoy casi seguro que no debo dereferenciar acá, pero tenía bugs y me funcionó al poner
    // la dereferencia, so I'm biased
    SWITCH_SetInterruptHandler(*set_pwm_duty_cycle);

    TMR0_PeriodMatchCallbackRegister(*Timer_Callback);
    TMR0_TMRInterruptEnable();
    TMR0_Start();

    TMR2_Start();

    while(1)
    {
    }    
}