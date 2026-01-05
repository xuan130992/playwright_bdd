Feature: I create a new park mod
  Scenario Outline: I create a new Park mod successful
    Given I go to page mod management
    Then I click registration button
    Then I input information to create a new mod with <package_version>
    Then I upload <android_file> with <filepath_android>
    Then I upload <iOs_file> with <filepath_iOS>
    Then I upload <windowns_file> with <filepath_windowns>
    Then I upload <server_file> with <filepath_server>
    Then I click register button
    Then I can see new official mod

    Examples:
      |package_version|android_file|filepath_android|iOs_file|filepath_iOS|windowns_file|filepath_windowns|server_file|filepath_server|
    |1.0.1|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[3]|./tests/resourse/modfile/Modfile.unity3d|xpath =(//*[@class="p-button-label" and contains(text(),"Upload")])[3]|./tests/resourse/modfile/Modfile.unity3d|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[3]|./tests/resourse/modfile/Modfile.unity3d|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[3]|./tests/resourse/modfile/Modfile.unity3d|