using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KillerItem : MonoBehaviour
{
	void Start()
	{
		List listV<Vector3>=new List<Vector3>;
		listV.Add(new Vector3(0,0,0));
		listV.Add(new Vector3(-0.5f,1,0));
		listV.Add(new Vector3(0.5f,1,0));
		listV.Add(new Vector3(0.5f,2,0));
		listV.Add(new Vector3(-0.5f,2,0));
		listV.Add(new Vector3(0,3,0));
		foreach (Vector3 v in listV)
		{
			GameObject.CreatePrimitive(PrimitiveType.Cube).transform.position = v;

		}
	}
	void Update(){}
}