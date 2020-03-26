/**
 * Used to create a image container that fits the image to it's outside container
 */

import 'package:flutter/material.dart';

class AssetImageContainer extends StatelessWidget {
  final String assetName;

  AssetImageContainer(this.assetName);

  @override
  Widget build(BuildContext context) {
    Container image = Container(
      // add a decoration to the container
      decoration: BoxDecoration(
        image: DecorationImage(
          //this fits the image to it's container
          fit: BoxFit.cover,
          //get the asset
          image: AssetImage(assetName)
        )
      ),
    );
    return image;
  }
}