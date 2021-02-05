import QtQuick 2.0

Item {
    width: 150
    height: 150

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 150
        height: 150
        color: "#ffffff"
        radius: 17
        border.width: 0

        Text {
            id: text1
            x: 53
            y: 66
            text: qsTr("RESET")
            font.pixelSize: 15
        }
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:6}
}
##^##*/
