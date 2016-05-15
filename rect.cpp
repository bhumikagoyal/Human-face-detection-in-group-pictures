#include <iostream>
#include <vector>
#include<stdlib.h>
#include<stdio.h>
#include<string>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <fstream>
#include<iostream>

void FindBlobs(const cv::Mat &binary, std::vector < std::vector<cv::Point2i> > &blobs);

int main(int argc, char **argv)
{
    cv::Mat img = cv::imread("gray_image1.png", 0); // force greyscale

    if(!img.data) {
        std::cout << "File not found" << std::endl;
        return -1;
    }

    cv::namedWindow("binary");
    cv::namedWindow("labelled");

    cv::Mat output = cv::Mat::zeros(img.size(), CV_8UC3);

    cv::Mat binary;
    std::vector < std::vector<cv::Point2i > > blobs;

    cv::threshold(img, binary, 0.0, 1.0, cv::THRESH_BINARY);

    FindBlobs(binary, blobs);
	std::ofstream myfile;
	myfile.open("examples.txt");
	
    // Randomy color the blobs
    for(size_t i=0; i < blobs.size(); i++) {
        unsigned char r = 255 * (rand()/(1.0 + RAND_MAX));
        unsigned char g = 255 * (rand()/(1.0 + RAND_MAX));
        unsigned char b = 255 * (rand()/(1.0 + RAND_MAX));
	std::cout<<blobs[i].size()<<"\n";
       if(blobs[i].size()>=100 && blobs[i].size()<=800){
            int x = blobs[i][0].x;
            int y = blobs[i][0].y;
		std::cout<<x<<"'"<<y<<"\n";
		std::string buffer,buffer1;
		 buffer=std::to_string(x);
	buffer1=std::to_string(y);
		myfile<<buffer<<","<<buffer1<<"\n";
	std::cout<<"lets";
	}	
         
        }
    

    myfile.close();
    cv::imshow("binary", img);
    cv::imshow("labelled", output);
    cv::waitKey(0);

    return 0;
}

void FindBlobs(const cv::Mat &binary, std::vector < std::vector<cv::Point2i> > &blobs)
{
    blobs.clear();

    // Fill the label_image with the blobs
    // 0  - background
    // 1  - unlabelled foreground
    // 2+ - labelled foreground

    cv::Mat label_image;
    binary.convertTo(label_image, CV_32SC1);

    int label_count = 2; // starts at 2 because 0,1 are used already

    for(int y=0; y < label_image.rows; y++) {
        int *row = (int*)label_image.ptr(y);
        for(int x=0; x < label_image.cols; x++) {
            if(row[x] != 1) {
                continue;
            }

            cv::Rect rect;
            cv::floodFill(label_image, cv::Point(x,y), label_count, &rect, 0, 0, 4);

            std::vector <cv::Point2i> blob;

            for(int i=rect.y; i < (rect.y+rect.height); i++) {
                int *row2 = (int*)label_image.ptr(i);
                for(int j=rect.x; j < (rect.x+rect.width); j++) {
                    if(row2[j] != label_count) {
                        continue;
                    }

                    blob.push_back(cv::Point2i(j,i));
                }
            }

            blobs.push_back(blob);

            label_count++;
        }
    }
}


