*** Variables ***
${search}     accessibility_id=Search
${noThanksOption1}    xpath=//android.widget.TextView[contains(@text,'No Thanks')]
${noThanksOption2}    xpath=//*[contains(@text,'No Thanks')]
${searchInput}        id=com.google.android.youtube:id/search_edit_text 
${firstVideo}         xpath=(//android.view.ViewGroup[contains(@content-desc,'<textElement>')])[1]
${pauseVideo}         accessibility_id=Pause video
${moreOptionsElement}    //android.widget.ImageView[contains(@content-desc,'options')] 
${resolution}          //android.widget.TextView[contains(@text,'Quality')]/following-sibling::android.widget.TextView[@instance='3']
${playbackSpeedElement}       //android.widget.TextView[contains(@text,'Playback speed')]/following-sibling::android.widget.TextView[@index='3']
${playVideoElement}      accessibility_id=Play video
${countdownText}      //android.widget.TextView[contains(@resource-id,'countdown_text')]
${adSkipElement}      //android.widget.TextView[contains(@resource-id,'skip')]
${videoPlaySlideBar}      //android.widget.TextView[contains(@resource-id,'time_bar_current_time')]