import 'package:flutter/material.dart';
import 'package:link/photoGallery.dart';
import 'photoGallery.dart' as PhotoGallery;
import 'groupList.dart' as GroupList;
import 'asset_image_container.dart' as AssetImageContainer;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // TODO make this an actual homepage of some sort, for now include widgets to see how they look for UI purposes
        title: Container(alignment: Alignment.center, child: Text("Testing page")),
      ),


      // you should see my handsome nephew brucie
      //adjust height and width to see how the picture adapts to the box around it
      body: Align(alignment: Alignment.center, child: Container(height: 300, width: 300, child: AssetImageContainer.AssetImageContainer("assets/debugging_pics/bruce_cigar.jpg")
    )),// This trailing comma makes auto-formatting nicer for build methods.

    // entire picture
//      body: Align(alignment: Alignment.center, child: AssetImageContainer.AssetImageContainer("assets/debugging_pics/bruce_cigar.jpg")),// This trailing comma makes auto-formatting nicer for build methods.

      // you should see a gallery of dogs
//      body: PhotoGallery.PhotoGallery(),


      // you should see an example contact list
//      body : GroupList.GroupList()

    );
  }
}

