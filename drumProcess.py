from PyQt4 import QtGui
import sys
from time import sleep
import drumMachine
import wave, pyaudio


class DrumMachineApp(QtGui.QMainWindow, drumMachine.Ui_Dialog):
    def __init__(self, parent=None):
        super(DrumMachineApp, self).__init__(parent)
        self.setupUi(self)

        # Parameters
        self.tempo = 120
        self.delay_time = 0.125
        self.playBeat = False
        # A 5(row)x16(col) Matrix
        self.Matrix = [[0 for x in range(16)] for y in range(5)]

        # Sequencer Buttons
        self.push_1_1.clicked.connect(lambda: self.changeColor(1, 1))
        self.push_1_2.clicked.connect(lambda: self.changeColor(1, 2))
        self.push_1_3.clicked.connect(lambda: self.changeColor(1, 3))
        self.push_1_4.clicked.connect(lambda: self.changeColor(1, 4))
        self.push_1_5.clicked.connect(lambda: self.changeColor(1, 5))
        self.push_1_6.clicked.connect(lambda: self.changeColor(1, 6))
        self.push_1_7.clicked.connect(lambda: self.changeColor(1, 7))
        self.push_1_8.clicked.connect(lambda: self.changeColor(1, 8))
        self.push_1_9.clicked.connect(lambda: self.changeColor(1, 9))
        self.push_1_10.clicked.connect(lambda: self.changeColor(1, 10))
        self.push_1_11.clicked.connect(lambda: self.changeColor(1, 11))
        self.push_1_12.clicked.connect(lambda: self.changeColor(1, 12))
        self.push_1_13.clicked.connect(lambda: self.changeColor(1, 13))
        self.push_1_14.clicked.connect(lambda: self.changeColor(1, 14))
        self.push_1_15.clicked.connect(lambda: self.changeColor(1, 15))
        self.push_1_16.clicked.connect(lambda: self.changeColor(1, 16))
        self.push_2_1.clicked.connect(lambda: self.changeColor(2, 1))
        self.push_2_2.clicked.connect(lambda: self.changeColor(2, 2))
        self.push_2_3.clicked.connect(lambda: self.changeColor(2, 3))
        self.push_2_4.clicked.connect(lambda: self.changeColor(2, 4))
        self.push_2_5.clicked.connect(lambda: self.changeColor(2, 5))
        self.push_2_6.clicked.connect(lambda: self.changeColor(2, 6))
        self.push_2_7.clicked.connect(lambda: self.changeColor(2, 7))
        self.push_2_8.clicked.connect(lambda: self.changeColor(2, 8))
        self.push_2_9.clicked.connect(lambda: self.changeColor(2, 9))
        self.push_2_10.clicked.connect(lambda: self.changeColor(2, 10))
        self.push_2_11.clicked.connect(lambda: self.changeColor(2, 11))
        self.push_2_12.clicked.connect(lambda: self.changeColor(2, 12))
        self.push_2_13.clicked.connect(lambda: self.changeColor(2, 13))
        self.push_2_14.clicked.connect(lambda: self.changeColor(2, 14))
        self.push_2_15.clicked.connect(lambda: self.changeColor(2, 15))
        self.push_2_16.clicked.connect(lambda: self.changeColor(2, 16))
        self.push_3_1.clicked.connect(lambda: self.changeColor(3, 1))
        self.push_3_2.clicked.connect(lambda: self.changeColor(3, 2))
        self.push_3_3.clicked.connect(lambda: self.changeColor(3, 3))
        self.push_3_4.clicked.connect(lambda: self.changeColor(3, 4))
        self.push_3_5.clicked.connect(lambda: self.changeColor(3, 5))
        self.push_3_6.clicked.connect(lambda: self.changeColor(3, 6))
        self.push_3_7.clicked.connect(lambda: self.changeColor(3, 7))
        self.push_3_8.clicked.connect(lambda: self.changeColor(3, 8))
        self.push_3_9.clicked.connect(lambda: self.changeColor(3, 9))
        self.push_3_10.clicked.connect(lambda: self.changeColor(3, 10))
        self.push_3_11.clicked.connect(lambda: self.changeColor(3, 11))
        self.push_3_12.clicked.connect(lambda: self.changeColor(3, 12))
        self.push_3_13.clicked.connect(lambda: self.changeColor(3, 13))
        self.push_3_14.clicked.connect(lambda: self.changeColor(3, 14))
        self.push_3_15.clicked.connect(lambda: self.changeColor(3, 15))
        self.push_3_16.clicked.connect(lambda: self.changeColor(3, 16))
        self.push_4_1.clicked.connect(lambda: self.changeColor(4, 1))
        self.push_4_2.clicked.connect(lambda: self.changeColor(4, 2))
        self.push_4_3.clicked.connect(lambda: self.changeColor(4, 3))
        self.push_4_4.clicked.connect(lambda: self.changeColor(4, 4))
        self.push_4_5.clicked.connect(lambda: self.changeColor(4, 5))
        self.push_4_6.clicked.connect(lambda: self.changeColor(4, 6))
        self.push_4_7.clicked.connect(lambda: self.changeColor(4, 7))
        self.push_4_8.clicked.connect(lambda: self.changeColor(4, 8))
        self.push_4_9.clicked.connect(lambda: self.changeColor(4, 9))
        self.push_4_10.clicked.connect(lambda: self.changeColor(4, 10))
        self.push_4_11.clicked.connect(lambda: self.changeColor(4, 11))
        self.push_4_12.clicked.connect(lambda: self.changeColor(4, 12))
        self.push_4_13.clicked.connect(lambda: self.changeColor(4, 13))
        self.push_4_14.clicked.connect(lambda: self.changeColor(4, 14))
        self.push_4_15.clicked.connect(lambda: self.changeColor(4, 15))
        self.push_4_16.clicked.connect(lambda: self.changeColor(4, 16))
        self.push_5_1.clicked.connect(lambda: self.changeColor(5, 1))
        self.push_5_2.clicked.connect(lambda: self.changeColor(5, 2))
        self.push_5_3.clicked.connect(lambda: self.changeColor(5, 3))
        self.push_5_4.clicked.connect(lambda: self.changeColor(5, 4))
        self.push_5_5.clicked.connect(lambda: self.changeColor(5, 5))
        self.push_5_6.clicked.connect(lambda: self.changeColor(5, 6))
        self.push_5_7.clicked.connect(lambda: self.changeColor(5, 7))
        self.push_5_8.clicked.connect(lambda: self.changeColor(5, 8))
        self.push_5_9.clicked.connect(lambda: self.changeColor(5, 9))
        self.push_5_10.clicked.connect(lambda: self.changeColor(5, 10))
        self.push_5_11.clicked.connect(lambda: self.changeColor(5, 11))
        self.push_5_12.clicked.connect(lambda: self.changeColor(5, 12))
        self.push_5_13.clicked.connect(lambda: self.changeColor(5, 13))
        self.push_5_14.clicked.connect(lambda: self.changeColor(5, 14))
        self.push_5_15.clicked.connect(lambda: self.changeColor(5, 15))
        self.push_5_16.clicked.connect(lambda: self.changeColor(5, 16))

        # Play/Stop Buttons
        self.pushPlay.clicked.connect(lambda: self.play())
        self.pushReset.clicked.connect(lambda: self.reset())
        self.pushStop.clicked.connect(lambda: self.stop())

        # BPM Control
        self.pushDownTempo.clicked.connect(lambda: self.setBPM(-1))
        self.pushUpTempo.clicked.connect(lambda: self.setBPM(1))
        self.lineEditTempo.returnPressed.connect(lambda: self.setBPM(0))

    def changeColor(self, row, col):
        if self.Matrix[row-1][col-1] == 0:
            exec("self.push_" + str(row) + '_' + str(col) + ".setStyleSheet('background-color: orange')")
            self.Matrix[row-1][col-1] = 1
        else:
            exec ("self.push_" + str(row) + '_' + str(col) + ".setStyleSheet('background-color: light gray')")
            self.Matrix[row-1][col-1] = 0

    # Play/Stop Functions
    def play(self, subbeat=0):
        self.playBeat = True
        while self.playBeat is True:
            subbeat = (subbeat % 16) + 1

            # update slider
            self.progressBar.setValue(subbeat)

            # update beat number
            if subbeat == 1:
                self.lcdnumberBeat.display(1)
            elif subbeat == 5:
                self.lcdnumberBeat.display(2)
            elif subbeat == 9:
                self.lcdnumberBeat.display(3)
            elif subbeat == 13:
                self.lcdnumberBeat.display(4)

            played = False
            # play sounds
            for sound in range(1, 6):
                if self.Matrix[sound-1][subbeat-1] == 1 and played is False:
                    self.playAudio(sound)
                    played = True

            # check for QtGui updates (especially stopping the drum machine)
            QtGui.QApplication.processEvents()
            if self.playBeat is False:
                break

            # Time Delay
            sleep(self.delay_time)

            # # NUMBA 2 :: check for QtGui updates (especially stopping the drum machine)
            # QtGui.QApplication.processEvents()
            # if self.playBeat is False:
            #     break
        # END while loop

    def playAudio(self, sound):
        if sound == 1:
            f = wave.open("audio/korg/MX drum/BD/033 BD-hip.wav", "rb")
        elif sound == 2:
            f = wave.open("audio/korg/MX drum/SD/043 SD-99 2.wav", "rb")
        elif sound == 3:
            f = wave.open("audio/korg/MX drum/RM/082 RM-Ambi1.wav", "rb")
        elif sound == 4:
            f = wave.open("audio/korg/MX drum/HH/095 HH-99 1C.wav", "rb")
        elif sound == 5:
            f = wave.open("audio/korg/MX drum/Rid/122 Rid-99 2.wav", "rb")
        else:
            return

        chunk = 1024
        # instantiate PyAudio
        p = pyaudio.PyAudio()

        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)

        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        # stop stream
        stream.stop_stream()
        stream.close()

    def stop(self):
        self.playBeat = False
        self.progressBar.setValue(0)

    def reset(self):
        self.playBeat = False
        self.progressBar.setValue(0)
        self.Matrix = [[0 for col in range(16)] for row in range(5)]
        for row in range(1, 6):
            for col in range(1, 17):
                exec ("self.push_" + str(row) + '_' + str(col) + ".setStyleSheet('background-color: light gray')")

    # BPM Functions
    def setBPM(self, status):
        if status != 0:
            self.tempo += status
            # update display
            self.lineEditTempo.setText(str(self.tempo))
        else:
            self.tempo = int(self.lineEditTempo.text())

        self.delay_time = 60.0 / (float(self.tempo) * 4.0)


def main():
    app = QtGui.QApplication(sys.argv)
    form = DrumMachineApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
