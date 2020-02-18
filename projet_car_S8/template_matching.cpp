#include <stdio.h>
#include <cv.h>
#include <highgui.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>


CvPoint templateMatching(char*filename,IplImage* image_capture,int test){
  double minVal;
  double maxVal;
  CvPoint minLoc; // position du minimum du template matching
  CvPoint maxLoc; // position du maximum du template matching
  CvSize taille; //taille de l'image template matching
  IplImage* templ;
  templ = cvLoadImage(filename);
  if(templ == NULL){
    printf("impossible d'ouvrir le fichier\n\7"); // Si la prise d'image n'est pas possible, on sort !
    cvSaveImage(filename, image_capture); //on sauvegarde pour pouvoir créer les templates
    exit(0);
  }
  //création matrice template matching
  taille.width =  image_capture->width - templ->width + 1;
  taille.height = image_capture->height - templ->height + 1;
  if (test==1) {
    printf("la taille est %d,%d\n",image_capture->width,image_capture->height);
  }
  IplImage*result_matching  = cvCreateImage(taille,IPL_DEPTH_32F ,1);
  cvMatchTemplate(image_capture,templ, result_matching, CV_TM_SQDIFF_NORMED);
  cvNormalize( result_matching, result_matching, 0, 1, CV_MINMAX);
  cvMinMaxLoc( result_matching, &minVal, &maxVal, &minLoc, &maxLoc);
  if(test==1)
  {
    cvSet2D(result_matching,minLoc.y,minLoc.x,255);
    cvCircle(result_matching,minLoc, 10, 255);
    if (strlen(filename)>10)
     {
    cvNamedWindow(filename, CV_WINDOW_AUTOSIZE);
    cvShowImage(filename, result_matching);
    printf("minloc =(%d,%d)\n",minLoc.x,minLoc.y);
    cvWaitKey(0);
  }
  }
  minLoc.x+=(int)((templ->width)/2);
  minLoc.y+=(int)((templ->height)/2);
  cvReleaseImage(&result_matching);
  cvReleaseImage(&templ);

  return minLoc;
}

CvPoint optimisation(char*filename,IplImage* image_capture,int test,IplImage* image_observation,int zone_observation,CvPoint position_avant)
{
  int position1x;
  int position2x;
  int position1y;
  int position2y;
  CvPoint position;
  int i;
  int j;
    //printf("image_capture->%d\n",image_capture->width);
  if (zone_observation>position_avant.x)
  {
    //printf("1, position 1x=%d, position 2x= %d,\n",0,2*zone_observation+1);
    position1x = 0;
    position2x = 2*zone_observation+1;
    position_avant.x= zone_observation;
  }
  else if ((image_capture->width-zone_observation)<=position_avant.x)
  {
      //printf("2, position 1x=%d, position 2x= %d,\n",image_capture->width-2*zone_observation+1,image_capture->width);
    //printf("image_capture->%d\n",image_capture->width);
    position1x = image_capture->width-2*zone_observation+1;
    position2x = image_capture->width;
    position_avant.x= image_capture->width - zone_observation;
  }
  else
  {
    //printf("3, position 1x=%d, position 2x= %d,\n",position_avant.x-zone_observation,position_avant.x+zone_observation);
    position1x = position_avant.x-zone_observation;
    position2x = position_avant.x+zone_observation+1;
  }
  if (zone_observation>position_avant.y)
  {

    position1y = 0;
    position2y = 2*zone_observation+1;
    //printf("4, position 1y=%d, position 2y= %d,\n",position1y,position2y);
    position_avant.y= zone_observation;
  }
  else if ((image_capture->height-zone_observation)<=position_avant.y)
  {
    position1y = image_capture->height-2*zone_observation+1;
    position2y = image_capture->height;
    //printf("5, position 1y=%d, position 2y= %d,\n",position1y,position2y);
      position_avant.y= image_capture->height - zone_observation;
  }
  else
  {
    position1y = position_avant.y-zone_observation;
    position2y = position_avant.y+zone_observation+1;
    //printf("6, position 1y=%d, position 2y= %d,\n",position1y,position2y);
  }
  for (i=position1x;i<position2x;i++)
  {
    for (j=position1y;j<position2y;j++)
    {
      if (test==1)
      {

        //printf("la position sur l'image originale est x = %d, y = %d\n",i,j);
        //printf("la position sur image opt est x = %d, y= %d\n",i-position1x,j-position1y);
      }
      cvSet2D(image_observation,j-position1y,i-position1x,cvGet2D(image_capture,j,i));
    }
  }
  if (test==1){
  printf("la position sur l'image originale est x = %d, y = %d\n",i,j);
  //printf("la position sur image opt est x = %d, y= %d\n",i-position1x,j-position1y);
}
position = templateMatching(filename,image_observation,test);

  position.x+=position_avant.x-zone_observation;
  position.y+=position_avant.y-zone_observation;
  return position;
}



int main(int argc, char *argv[])
{
  /* On initialise la 'capture' depuis la WebCam, une adresse,
  représentative de la ressource est retournée
  */
  FILE* fichier = NULL;
  int webcam = 0;
  int test=0;
  int temps=0;
  double a=1.0;
  if(argc==5){
    sscanf(argv[1],"%d",&test);
    sscanf(argv[2],"%d",&webcam);
    sscanf(argv[3],"%lf",&a);
    sscanf(argv[4],"%d",&temps);
  }
  CvCapture* capture;
  //cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 1920);
  //cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 1080);

  char photo_avant[] = "template_avant.png";
  char photo_arriere[] = "template_arriere.png";
  char photo_arrivee[] = "template_arrivee.png";
  CvPoint avant;
  CvPoint arriere;
  CvPoint arrivee;
  IplImage *image_capture;
  double x;
  double y;
  double angle;
  double distance1;
  int init =1;
  CvSize taille;
  CvScalar couleur;
  int zone_observation = 130;
  taille.width =  zone_observation*2+1;
  taille.height = zone_observation*2+1;
  IplImage* image_observation = cvCreateImage(taille,IPL_DEPTH_8U ,3);
  capture = cvCaptureFromCAM(webcam);
  cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 1920);
  cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 1080);
  //cvSetCaptureProperty(capture, CV_CAP_PROP_BUFFERSIZE,3);
  do {

    if(capture) // Si la caméra est reconnu
    {
      //fflush(stdin);
      image_capture = cvQueryFrame(capture); //on prends une image
        //cvSet2D(image_capture,50,50,cvScalar( 0, 0, 0 ));
      if (test==2 || test ==1)
        {
      cvCircle(image_capture,arriere, 100, cvScalar( 0, 10, 10 ),1);
      cvCircle(image_capture,avant, 105, cvScalar( 0, 0, 255),1);
      cvCircle(image_capture,arrivee, 110, cvScalar( 255, 0, 0),1);
      cvShowImage("video",image_capture);
      cvWaitKey(1);
        }
      if(image_capture==NULL)
      {
        printf("impossible de capturer une photo\n\7"); // Si la prise d'image n'est pas possible, on sort !
        exit(0);
      }
    }
    else // Si la caméra n'est pas reconnu ou si elle n'existe pas, on sort...
    {
      printf("impossible de faire fonctionner l'appareil de capture video\n");
      exit(0);
    }
    if(test==1)
    {
      // On crée une fenètre dans laquelle on affichera l'image
      //cvNamedWindow("Fenetre_test", CV_WINDOW_AUTOSIZE);

      // C'est ce que l'on fait ici :
      //cvShowImage("Fenetre_test", image_capture );
    }
    if (init==1)
    {
      avant = templateMatching(photo_avant,image_capture,test);
      arriere = templateMatching(photo_arriere,image_capture,test);
      arrivee = templateMatching(photo_arrivee,image_capture,test);
      cvReleaseCapture(&capture);
      capture = cvCaptureFromCAM(webcam);
      cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 1920);
      cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 1080);
      //cvSetCaptureProperty(capture, CV_CAP_PROP_BUFFERSIZE,3);
    }
    else {
      avant = optimisation(photo_avant,image_capture,test,image_observation,zone_observation,avant);
      arriere = optimisation(photo_arriere,image_capture,test,image_observation,zone_observation,arriere);
      arrivee = optimisation(photo_arrivee,image_capture,test,image_observation,zone_observation,arrivee);
      //printf("arrivee : x= %d, y = %d\n",arrivee.x,arrivee.y);
    }
    x = avant.x-arriere.x;
    y = avant.y-arriere.y;
    distance1 = sqrt(x*x+y*y);
    //printf(" avant= (%d, %d) \n arriere = (%d, %d) \n arrivee (%d %d)\n",avant.x,avant.y,arriere.x,arriere.y,arrivee.x,arrivee.y);
    if (distance1>2000|| distance1<0)
    {
      init=1;
    }
    else
    {
      init = 0;
      angle = acos(x/distance1)*360.0/(2.0*3.14159265);
      fichier = fopen("valeurs.txt", "w");
      fprintf(fichier,"%lf %lf  %lf %lf %lf \n",a*(avant.x+a*arriere.x)/2.0,a*(avant.y+arriere.y)/2.0,a*arrivee.x,a*arrivee.y,angle);
      if(test==1)
      {
        printf("distance = %d pixels\n",(int)distance1);
        printf(" avant= (%d, %d) \n arriere = (%d, %d) \n arrivee (%d %d)\n",avant.x,avant.y,arriere.x,arriere.y,arrivee.x,arrivee.y);
        printf("a= %lf\n",a);
        //printf("%lf %lf  %lf %lf %lf \n",a*(avant.x+a*arriere.x)/2.0,a*(avant.y+arriere.y)/2.0,a*arrivee.x,a*arrivee.y,angle);

        //cvWaitKey(0);
      }
      fclose(fichier);
    }
  } while(temps==1);
  cvReleaseImage(&image_capture);
  cvReleaseCapture(&capture);

  // On libère ensuite, la mémoire de l'image et de la ressource

  return 0;
}
