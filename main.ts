input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    music.play(music.tonePlayable(277, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    music.play(music.tonePlayable(784, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
})
