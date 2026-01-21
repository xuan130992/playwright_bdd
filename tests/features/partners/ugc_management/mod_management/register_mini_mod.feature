Feature: I create a new mini mod
  Scenario Outline: I create a new mini mod successful
    Given I go to page mod management
    Then I click registration button
    Then I input information to create a new mod with <package_version> and <eng_description>
    Then I click add screenshot button
    Then I upload <screenshot_image> with <filepath_image>
    Then I upload <android_file> with <filepath_android>
    Then I upload <iOs_file> with <filepath_iOS>
    Then I upload <windowns_file> with <filepath_windowns>
    Then I upload <server_file> with <filepath_server>
    Then I click register button
    Then I can see new official mod
    Examples:
      |package_version|eng_description|screenshot_image|filepath_image|android_file|filepath_android|iOs_file|filepath_iOS|windowns_file|filepath_windowns|server_file|filepath_server|
      |101|Eng_des_mod_1|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/modfile/17_optimized.png|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/modfile/Modfile.unity3d|xpath =(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/modfile/Modfile.unity3d|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/modfile/Modfile.unity3d|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/modfile/Modfile.unity3d|
