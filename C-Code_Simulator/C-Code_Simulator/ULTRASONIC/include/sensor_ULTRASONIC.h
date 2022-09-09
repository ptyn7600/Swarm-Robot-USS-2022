#ifndef SENSOR_ULTRASONIC_H   
#define SENSOR_ULTRASONIC_H    /* prevents the file from being included twice. */
/* Including a header file twice causes all kinds */
/* of interesting problems.*/
/*
*  state_size : the size of the finite numbers of the state used in the Bayesian Filter: d = {0, 0.1, 0.2, ... , 59.8, 59.9}
*/
#define state_size  591


/*
 * Function:  summ_array
 * --------------------
 * computes the sum of all elements in a given array
 *
 *  array[]: the array to be sum
 *  num_elements: size of the given array
 *  returns: the sum of the given array as a single double
 *           returns zero if array is emtpy
 */
double sum_array(double array[], int num_elements);


/*
 * Function:  normalize_array
 * --------------------
 * normalize the given array by dividing all the elements by the sum of them
 *
 *  array[]: the array to be sum
 *  num_elements: size of the given array
 *  returns: void
 */
void normalize_array(double array[], int num_elements);

/*
 * Function:  make_prediction
 * --------------------
 * computes the probability array of finite numbers of state given a reading. The probability retains and only resets after 10 iterations or restart parameter is set to 1.
 *
 *  reading: the reading of the sensors (ultrasonic, IR, etc.)
 *  restart: 1 to restart the probability array. Otherwise, default is 0
 *  returns: the probability array of finite numbers of state
 */
double* make_prediction(double reading, int restart);

/*
 * Function:  randnorm
 * --------------------
 * generate a random number that follows a normal distribution with a given mean and standard deviation
 *
 *  mu: mean of the normal distribution
 *  sigma: standard deviation of the normal distribution
 *  returns: a single double that is taken from a normal distribution with a given mean and standard deviation
 */
double randnorm(double mu, double sigma);

 /* Function:  generate_data
 * --------------------
 * generate a random number that follows a normal distribution with a mean and standard deviation calculated based on a given distance. 
 *
 *  distance: distance of the object measured from the sensor
 *  returns: a single double that is taken from a normal distribution with a calculated mean and standard deviation
 */
double generate_data(double distance);

 /* Function:  generate_data_set
 * --------------------
 * generate an array of random numbers that follows a normal distribution with a mean and standard deviation calculated based on a given distance. 
 *	
 *	numberSample: the size of the output array of random numbers
 *  distance: distance of the object measured from the sensor
 *  returns: a array of random doubles that is taken from a normal distribution with a calculated mean and standard deviation
 */
double* generate_data_set(double distance, int numberSample);

 /* Function:  printArr
 * --------------------
 * print the given array  
 *	
 *	arr[]: the array to be printed
 *  size: size of the array to be printed
 *  returns: void
 */
void printArr(double arr[], int size);


#endif /* SENSOR_ULTRASONIC_H */