#include <stdio.h> // Pour le printf()...

/* Les deux bibliothèques nécessaires d'opencv :
	- cv.h contient les structures et fonctions de manipulation d'images
	- highgui.h contient les fonctions d'affichage des images
*/
#include <cv.h>
#include <highgui.h>

int main(int argc, char *argv[])
{
  /* On initialise la 'capture' depuis la WebCam, une adresse,
     représentative de la ressource est retournée
   */
  CvCapture* capture = cvCaptureFromCAM(-1);
  if(capture) // Si la caméra est reconnu
  {
	/*if(!cvGrabFrame(capture)) // On prend une image et une seule !
	{
  		printf("Could not grab a frame\n\7"); // Si la prise d'image n'est pas possible, on sort !
  		exit(0);
	}*/
  }
  else // Si la caméra n'est pas reconnu ou si elle n'existe pas, on sort...
  {
  	printf("Could not open video device\n");
  	exit(0);
  }
	IplImage *img=cvRetrieveFrame(capture); // On rapatrie l'image que l'on 'stocke' dans img avec ses propriétés.

  printf("L'image fait %dx%d pixels et possède %d canaux (couleurs)\n",img->width,img->height,img->nChannels);

  // On crée une fenètre dans laquelle on affichera l'image
  cvNamedWindow("Fenetre_test", CV_WINDOW_AUTOSIZE);

  // C'est ce que l'on fait ici :
  cvShowImage("Fenetre_test", img );
  // Appuyez sur une touche pour sortir
  cvWaitKey(0);

  // On libère ensuite, la mémoire de l'image et de la ressource
  cvReleaseImage(&img );
  cvReleaseCapture(&capture);
  return 0;
}
































#include <stdio.h>
#include <cv.h>
#include <highgui.h>

int main(int argc, char *argv[])
{
  /* On initialise la 'capture' depuis la WebCam, une adresse,
     représentative de la ressource est retournée
   */
  IplImage *image_capture;
  IplImage* templ;
  CvCapture* capture = cvCaptureFromCAM(-1);
  double minVal;
  double maxVal;
  CvPoint minLoc;
  CvPoint maxLoc;
  char photo_avant[] = "template_avant.png";
  char photo_ariere[] = "template_arriere.png"
  char photo_arrive[] =
  if(capture) // Si la caméra est reconnu
  {
    printf("4\n");
    image_capture = cvQueryFrame(capture); //on prends une image
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


  //printf("L'image fait %dx%d pixels et possède %d canaux (couleurs)\n",img->width,img->height,img->nChannels);

  // On crée une fenètre dans laquelle on affichera l'image
  cvNamedWindow("Fenetre_test", CV_WINDOW_AUTOSIZE);

  // C'est ce que l'on fait ici :
  cvShowImage("Fenetre_test", image_capture );
  // Appuyez sur une touche pour sortir
  //cvSaveImage(photo, image_capture);
  templ = cvLoadImage(photo);
  cvNamedWindow("Fenetre_test2", CV_WINDOW_AUTOSIZE);
  cvShowImage("Fenetre_test2", templ );
  CvSize taille;
   taille.width =  image_capture->width - templ->width + 1;
   taille.height = image_capture->height - templ->height + 1;
  IplImage*result_matching  = cvCreateImage(taille,IPL_DEPTH_32F ,1);
  cvMatchTemplate(image_capture,templ, result_matching, CV_TM_CCOEFF_NORMED);
  cvNormalize( result_matching, result_matching, 0, 1, CV_MINMAX);
  cvMinMaxLoc( result_matching, &minVal, &maxVal, &minLoc, &maxLoc);
  cvSet2D(result_matching,minLoc.y,minLoc.x,255);
  cvNamedWindow("Fenetre_test3", CV_WINDOW_AUTOSIZE);
  cvShowImage("Fenetre_test3", result_matching);
  cvWaitKey(0);

  // On libère ensuite, la mémoire de l'image et de la ressource
  cvReleaseImage(&image_capture );
  cvReleaseCapture(&capture);
  return 0;
}




cvPoint templateMatching(char*filename)
