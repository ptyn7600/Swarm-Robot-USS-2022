#ifndef SENSOR_IR_H   
#define SENSOR_IR_H    /* prevents the file from being included twice. */
/* Including a header file twice causes all kinds */
/* of interesting problems.*/
#define state_dist_size  21	// Column
#define state_angle_size 10  // Row

double sum_2Darray(double arr[][state_dist_size], int row, int column);
void normalize_2Darray(double arr[][state_dist_size], int row, int column);
double(*make_prediction(double reading, int restart))[state_dist_size];
double randnorm(double mu, double sigma);
double generate_data(double distance, double angle);
double* generate_data_set(double distance, double angle, int numberSample);
void print2DArr(double arr[][state_dist_size], int row, int column);


#endif /* SENSOR_IR_H */