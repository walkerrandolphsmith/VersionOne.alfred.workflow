# VersionOne.alfred.workflow
<img width="75" src="https://cloud.githubusercontent.com/assets/398893/3528722/5b5b30c6-0792-11e4-956d-750ac3a00bd8.png">

[Alfred 2](https://www.alfredapp.com/) Workflow for interacting with a [VersionOne](https://www.versionone.com/) instance. To learn more about the VersionOne API visit [the documentation site](https://community.versionone.com/Developers)

## Workflows

###Settings

Enter your VersionOne instance's url  
> Triggers: `v1url`  

Enter your VersionOne API token: 
//Example: Bearer XXXXXXXXXXX  
> Triggers: `v1token`

View your VersionOne instance's url
> Triggers: `v1 settings view url`

<img width="500" src="./screenshots/v1-settings-view-url.png">

Change your VersionOne instance's url
> Triggers: `v1 settings update url <new-url>`

<img width="500" src="./screenshots/v1-settings-update-url.png">


###Open pages and assets

 Open any page:
> Triggers: `v1 open pages`

<img width="500" src="./screenshots/v1-open-pages.png">

Open specific pages:
> Triggers: `v1 open backlog` | `v1 open reports` | `v1 open iteration scheduling`

<img width="500" src="./screenshots/v1-open-backlog.png">

Open lobby:
> Triggers: `v1 open lobby`

<img width="500" src="./screenshots/v1-open-lobby.png">

 Open team room by name:
> Triggers: `v1 open teamroom <teamroom-name>`

<img width="500" src="./screenshots/v1-open-teamroom.png">

 Lookup VersionOne assets by type and open asset
> Triggers: `v1 open epics` | `v1 open storys`

<img width="500" src="./screenshots/v1-open-asset-by-asset-type.png">

 Open VersionOne asset by oid
> Triggers: `v1 open story:12345`

<img width="500" src="./screenshots/v1-open-by-asset-oid.png">

 Open VersionOne asset by name
> Triggers: `v1 open <asset-type> <asset-name>`

<img width="500" src="./screenshots/v1-open-asset-by-name.png">


###Update assets

 Set single value relations to assets
 > Triggers: `v1 set <oid> <relation-name>`

 <img width="500" src="./screenshots/v1-set-single-value-relation-by-relation-name.png">