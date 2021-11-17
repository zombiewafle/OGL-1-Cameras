# GLSL

vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

#toonShader = """
#uniform vec3 lightDir;
#varying vec3 normal;
#
#void main()
#{
#	float intensity;
#	vec4 color;
#	intensity = dot(lightDir,normalize(normal));
#
#	if (intensity > 0.95)
#		color = vec4(1.0,0.5,0.5,1.0);
#	else if (intensity > 0.5)
#		color = vec4(0.6,0.3,0.3,1.0);
#	else if (intensity > 0.25)
#		color = vec4(0.4,0.2,0.2,1.0);
#	else
#		color = vec4(0.2,0.1,0.1,1.0);
#	gl_FragColor = color;
#
#}
#"""


fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""
