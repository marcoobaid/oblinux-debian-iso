/* SPDX-FileCopyrightText: 2026 OBLinux Project
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation
{
    id: presentation

    Slide {
        Image {
            id: background
            source: "slide1.png"
            width: 640
            height: 360
            fillMode: Image.PreserveAspectFit
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
        }
        Text {
            anchors.horizontalCenter: background.horizontalCenter
            anchors.top: background.bottom
            anchors.topMargin: 16
            text: qsTr("Installing OBLinux.<br/>" +
                       "The process should complete in a few minutes.")
            wrapMode: Text.WordWrap
            width: 640
            horizontalAlignment: Text.Center
        }
    }
}
