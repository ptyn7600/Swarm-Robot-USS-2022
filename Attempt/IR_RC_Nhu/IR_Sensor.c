/**
 * @file rc_project_template.c
 *
 * This is meant to be a skeleton program for Robot Control projects. Change
 * this description and file name before modifying for your own purpose.
 */

#include <stdio.h>
#include <robotcontrol.h> // includes ALL Robot Control subsystems

// function declarations
void on_pause_release();
void on_pause_press();

// global variable
// LED Setup
int ledPin = 25;
int ledChip = 1;
int ledState = 0;
// Button Setup
int buttonPin = 17;
int buttonChip = 1;
int oldButtonState = 0;
int distanceButton = 3;
// Onboard button
int onBoardButtonState = 0;
int fileopen = 0;
// Time
int echo = 0, previousEcho = 0, lowHigh = 0, highLow = 0;
long startTime, stopTime, difference;
double distance = 0;
int count = 0;
// Ultrasonic Setup
int echoPin = 2;
int echoChip = 3;
int trigPin = 1;
int trigChip = 3;
// IR sensor parameter
long read_ADC = 0;
int count_ADC= 0;
double distance_cm = 0;
double measureParam_k1 = 10599.39878314;
double measureParam_k2 = -0.91937492;

FILE *fpt;

void collectDataForDistribution(long data){
	fprintf(fpt,"%ld\n",data);
}

void collectData(){
	printf("Distance : %.2f ---> ADC reads %ld \n", distance_cm, read_ADC/100);
	fprintf(fpt,"%.2f,%ld\n",distance_cm , read_ADC/100);
	
	count = 0;
	read_ADC = 0;
	distance_cm += 0.5;
}

void rawDatatoDistance(double rawData){
	double returnValue = pow((rawData/measureParam_k1),(1/(measureParam_k2)));
	printf("Distance is %.2f\n", returnValue);
	count = 0;
	read_ADC = 0;
}

/**
 * This template contains these critical components
 * - ensure no existing instances are running and make new PID file
 * - start the signal handler
 * - initialize subsystems you wish to use
 * - while loop that checks for EXITING condition
 * - cleanup subsystems at the end
 *
 * @return     0 during normal operation, -1 on error
 */
int main()
{
	// make sure another instance isn't running
	// if return value is -3 then a background process is running with
	// higher privaledges and we couldn't kill it, in which case we should
	// not continue or there may be hardware conflicts. If it returned -4
	// then there was an invalid argument that needs to be fixed.
	if(rc_kill_existing_process(2.0)<-2) return -1;

	// start signal handler so we can exit cleanly
	if(rc_enable_signal_handler()==-1){
		fprintf(stderr,"ERROR: failed to start signal handler\n");
		return -1;
	}

	// initialize pause button
	if(rc_button_init(RC_BTN_PIN_PAUSE, RC_BTN_POLARITY_NORM_HIGH,
						RC_BTN_DEBOUNCE_DEFAULT_US)){
		fprintf(stderr,"ERROR: failed to initialize pause button\n");
		return -1;
	}
	
	// Assign functions to be called when button events occur
	rc_button_set_callbacks(RC_BTN_PIN_PAUSE,on_pause_press,on_pause_release);
	
	// make PID file to indicate your project is running
	// due to the check made on the call to rc_kill_existing_process() above
	// we can be fairly confident there is no PID file already and we can
	// make our own safely.
	rc_make_pid_file();

	// Set up ADC 
	rc_adc_init();

	// Keep looping until state changes to EXITING
	rc_set_state(RUNNING);

	while(rc_get_state()!=EXITING){
		while (onBoardButtonState) {
			onBoardButtonState = 0;
			char fileName[100];
			sprintf(fileName, "./data/%dcm_40degree.csv",distanceButton);
			printf("Distance is %d\n", distanceButton);
			fpt = fopen(fileName, "w+");
			fileopen = 1;
		}
		while(fileopen) {
			if (count < 10000) {
				long data =  rc_adc_read_raw(0);
				collectDataForDistribution(data);
				read_ADC += data;
				count++;
			} else {
				// // collectData();
				rawDatatoDistance(read_ADC/10000.0);
				//rc_usleep(4000000);
				// rc_usleep(4000000);
				fclose(fpt);
				fileopen = 0;
				// break;
			}
		}
		
	}

	// close file descriptors
	// fclose(fpt);
	rc_adc_cleanup();		// clean ADC subsystem
	rc_button_cleanup();	// stop button handlers
	rc_remove_pid_file();	// remove pid file LAST
	return 0;
}

// float distance_measurement(TRIG,ECHO) {
// }

/**
 * Make the Pause button toggle between paused and running states.
 */
void on_pause_release()
{
	onBoardButtonState = 1;
	distanceButton++;
}

/**
* If the user holds the pause button for 2 seconds, set state to EXITING which
* triggers the rest of the program to exit cleanly.
**/
void on_pause_press()
{
	int i;
	const int samples = 100; // check for release 100 times in this period
	const int us_wait = 2000000; // 2 seconds

	// now keep checking to see if the button is still held down
	for(i=0;i<samples;i++){
		rc_usleep(us_wait/samples);
		if(rc_button_get_state(RC_BTN_PIN_PAUSE)==RC_BTN_STATE_RELEASED) return;
	}
	printf("long press detected, shutting down\n");
	rc_set_state(EXITING);
	return;
}

