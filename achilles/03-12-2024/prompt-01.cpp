#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat whiteBalanceGrayWorld(const Mat &src)
{
    // Convert to float for precision
    Mat src_f;
    src.convertTo(src_f, CV_32F);

    // Compute the mean value for each channel
    Scalar channel_mean = mean(src_f);

    // Create scaling factors
    float scale_r = channel_mean[1] / channel_mean[0]; // Green / Blue
    float scale_b = channel_mean[1] / channel_mean[2]; // Green / Red

    // Create a scaling matrix
    Mat scaling_matrix = (Mat_<float>(3, 3) << scale_b, 0, 0,
                          0, 1, 0,
                          0, 0, scale_r);

    // Apply the scaling matrix
    Mat dst;
    transform(src_f, dst, scaling_matrix);

    // Convert back to 8-bit unsigned integer
    dst.convertTo(dst, CV_8U);

    return dst;
}

int mainA()
{
    Mat image = imread("./image.jpg");

    if (image.empty())
    {
        cerr << "Could not open or find the image" << endl;
        return -1;
    }

    Mat balanced_image = whiteBalanceGrayWorld(image);

    imshow("Original Image", image);
    imshow("White Balanced Image", balanced_image);
    waitKey(0);

    return 0;
}

void whiteBalance(cv::Mat & image)
{
    // Calculate the average color of the image
    cv::Scalar avgColor = cv::mean(image);

    // Calculate the scaling factors for each channel to make the average color gray
    double scaleFactor[3];
    for (int i = 0; i < 3; ++i)
    {
        scaleFactor[i] = avgColor[i] == 0 ? 0 : (128.0 / avgColor[i]);
    }

    // Apply the scaling factors to each pixel
    for (int y = 0; y < image.rows; ++y)
    {
        for (int x = 0; x < image.cols; ++x)
        {
            for (int c = 0; c < 3; ++c)
            {
                image.at<cv::Vec3b>(y, x)[c] = cv::saturate_cast<uchar>(scaleFactor[c] * image.at<cv::Vec3b>(y, x)[c]);
            }
        }
    }
}

int mainB()
{
    // Load the image
    cv::Mat image = cv::imread("./image.jpg");

    // Perform white balancing
    whiteBalance(image);

    // Save the result
    cv::imwrite("./result.jpg", image);

    return 0;
}

int main()
{
    mainA();
    mainB();
    return 0;
}