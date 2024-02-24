{
	"targets": [
		{
			"target_name": "node_windows_trayicon",
			"conditions": [
        		['OS=="win"', {
					"sources": [
						"TrayWrapper.cpp",
						"TrayIcon.cpp"
					],
					"include_dirs": [
						"<!@(node -p \"require('node-addon-api').include\")"
					],
					'msbuild_settings': {
						"ClCompile": {
							"RuntimeLibrary": "MultiThreaded"
						}
					}
				}]
			]
		},
		{
			"target_name": "action_after_build",
			"type": "none",
			"dependencies": [ "node_windows_trayicon" ],
			"copies": [
				{
					"files": [ "<(PRODUCT_DIR)/node_windows_trayicon.node" ],
					"destination": "./lib/binding/"
				}
			],
		}
	]
}
