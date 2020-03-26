/**
 * create the basic layout for a grid of photographs
 */

import 'package:flutter/material.dart';
import 'asset_images_mapping.dart' as AssetList;
import 'asset_image_container.dart' as ImageContainer;

class PhotoGallery extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    // get the screen's available width and height
    final double sizeWidth = MediaQuery.of(context).size.width;
    final double sizeHeight = MediaQuery.of(context).size.height;

    Stack widgets = Stack(
      children: <Widget>[
        Container(width: sizeWidth, height: sizeHeight,),
        Align(
          alignment: Alignment.topCenter,
          child: Container(
            width: sizeWidth,
            height: sizeHeight - sizeHeight / 4.0,
            child: GridView.builder(
              /**
              * TODO ; make the hard coded pixel values here with sizeWidth and
              * TODO : sizeHeight, also make certain values such as # of pics
              * TODO : per row customizable by the user
              */
              itemCount: 50,
              scrollDirection: Axis.vertical,
              padding: EdgeInsets.all(7.5),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                // TODO make this customized by the user
                crossAxisCount: 3,
                mainAxisSpacing: 7.5,
                crossAxisSpacing: 7.5,
              ),
              itemBuilder:   (BuildContext context, int index) => imageGetter(context, index),)),
        ),
        galleryButton(sizeHeight, sizeWidth),
      ]
    );
    return widgets;
//    Container(
//      width: sizeWidth,
//      height: sizeHeight - sizeHeight / 4.0,
//      child:
//      Container(alignment: Alignment.bottomCenter, child: GridView.builder(
//        /**
//         * TODO ; make the hard coded pixel values here with sizeWidth and
//         * TODO : sizeHeight, also make certain values such as # of pics
//         * TODO : per row customizable by the user
//         */
//        itemCount: 50,
//        scrollDirection: Axis.vertical,
//        padding: EdgeInsets.all(7.5),
//        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
//          // TODO make this customized by the user
//          crossAxisCount: 3,
//          mainAxisSpacing: 7.5,
//          crossAxisSpacing: 7.5,
//        ),
//        itemBuilder:   (BuildContext context, int index) => imageGetter(context, index),)),
//    ),

  }

  Widget imageGetter(BuildContext context, int index) {
    String assetName = AssetList.assetNames[index % AssetList.assetNames.length];
    return ImageContainer.AssetImageContainer(assetName);
  }

  Widget galleryButton(double sizeY, double sizeX) {
    Align button = Align(
      alignment: Alignment.bottomCenter,
        child: RaisedButton(
          elevation: 12,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          color: Colors.blue[300],
          child: Text("button 1",
              style: TextStyle(fontSize: 20, color: Colors.white)),
          onPressed: () {print("best dogs");},
        ));
    return button;
  }
}

