<!DOCTYPE html>
<html lang="en">
	<head>
		<title>three.js webgl - geometry - cube</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		<link type="text/css" rel="stylesheet" href="main.css">
	</head>
	<body>

		<!-- Import maps polyfill -->
		<!-- Remove this when import maps will be widely supported -->
		<script async src="https://unpkg.com/es-module-shims@1.3.6/dist/es-module-shims.js"></script>

		<script type="importmap">
			{
				"imports": {
					"three": "../build/three.module.js",
					"three/addons/": "./jsm/"
				}
			}
		</script>

		<script type="module">

			import * as THREE from 'three';

			let camera, scene, renderer;
			let mesh;

			init();
			animate();

			function init() {

				camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
				camera.position.z = 400;

				scene = new THREE.Scene();
				
				
				const texture_b = new THREE.TextureLoader().load( 'textures/4.png' );
				const texture_f = new THREE.TextureLoader().load( 'textures/0.png' );
				
				var geometry = new THREE.BoxGeometry( 200, 200, 1 );
				var materials = [
					new THREE.MeshBasicMaterial( { map: texture_f } ),
					new THREE.MeshBasicMaterial( { map: texture_f } ),
					new THREE.MeshBasicMaterial( { map: texture_f } ),
					new THREE.MeshBasicMaterial( { map: texture_f } ),
					new THREE.MeshBasicMaterial( { map: texture_f } ),
					new THREE.MeshBasicMaterial( { map: texture_b } )		//BACK
				];

				mesh = new THREE.Mesh( geometry, materials );
				scene.add( mesh );
                mesh.cursor = 'pointer';
                mesh.on('click'.function(ev){
                console.log('aa');
                })
                

				renderer = new THREE.WebGLRenderer( { antialias: true } );
				renderer.setPixelRatio( window.devicePixelRatio );
				renderer.setSize( window.innerWidth, window.innerHeight );
				document.body.appendChild( renderer.domElement );

				window.addEventListener( 'resize', onWindowResize );

			}

			function onWindowResize() {

				camera.aspect = window.innerWidth / window.innerHeight;
				camera.updateProjectionMatrix();

				renderer.setSize( window.innerWidth, window.innerHeight );

			}

			function animate() {
				console.log("animate");
				console.log("animate",camera.position);
				requestAnimationFrame( animate );

				mesh.rotation.z += 0.01;
				mesh.rotation.y += 0.01;

				renderer.render( scene, camera );

			}

		</script>

	</body>
</html>
