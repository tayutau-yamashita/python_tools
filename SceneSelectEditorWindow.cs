using UnityEngine;
using UnityEditor;
using UnityEditor.SceneManagement;
using System.Collections;
using System.Collections.Generic;

public class SceneSelectEditorWindow : EditorWindow {

	private class SceneData {
		public string DisplaySceneName = "";
		public string LoadScenePath = "";
	}
	List<SceneData> SceneNameList = new List<SceneData>();
	static SceneSelectEditorWindow This = null;
	private Vector2 ScrollPosition;

	[MenuItem ("Window/SceneSelectEditorWindow")]
	public static void ShowWindow () {
		This = EditorWindow.GetWindow(typeof(SceneSelectEditorWindow)) as SceneSelectEditorWindow;
		This.Initialize();
	}

	void Initialize () {
		Debug.Log ("---- SceneSelectEditorWindow:Initialize ----");
		SceneNameList.Clear();
		foreach (var guid in AssetDatabase.FindAssets("t:Scene")) {
			var path = AssetDatabase.GUIDToAssetPath (guid);
			if (path.IndexOf ("Test") != -1) {
				continue;
			}
			SceneData data = new SceneData();
			int index = path.LastIndexOf("/");
			string name = path;
			if (index != -1) {
				name = path.Remove(0, index+1);
			}
			data.DisplaySceneName = name;
			data.LoadScenePath = path;
			SceneNameList.Add(data);
//			Debug.Log(AssetDatabase.LoadMainAssetAtPath(path));
		}	
	}

	// Update is called once per frame
	void Update () {
	
	}

	void OnGUI () {
		EditorGUILayout.BeginVertical();

		//PropertyFieldを使えば、型に合わせて基本通り描画してくれる。
		//面倒なUndo処理とかも書かなくてもいい、
//		EditorGUILayout.PropertyField(serializedObject.FindProperty("customSize"), new GUIContent("Size"));
		ScrollPosition = EditorGUILayout.BeginScrollView(ScrollPosition, GUILayout.Height(200));
		for (int i = 0; i < SceneNameList.Count; i++) {
			if (GUILayout.Button(SceneNameList[i].DisplaySceneName, GUILayout.Width(200f))) {
				if (EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo()) {
					EditorSceneManager.OpenScene(SceneNameList[i].LoadScenePath);
				}
			}
		}

		EditorGUILayout.EndScrollView();
		EditorGUILayout.EndVertical();
	}
}
