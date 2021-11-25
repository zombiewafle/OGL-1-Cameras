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

psico_shader = """
#version 450
layout(location = 0) out vec4 fragColor;
in float intensity;
in vec2 vertexTexcoords;
in vec3 v3Position;
in float timer;
in vec3 fnormal;
uniform sampler2D tex;
uniform vec4 diffuse;
uniform vec4 ambient;

void main()
{
	float time = timer*0.5;
	float bright = floor(mod(v3Position.z, time)*time) +floor(mod(v3Position.y, time)*time);
	vec4 color = mod(bright, 1.5) > 0.007 ? vec4(0.0, 1.0, 0.0, 1.0) : vec4(1.0, 0.0, 1.0, 1.0);
  	fragColor = color * intensity;
}
"""

toon_shader = """
#version 450
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projectionMatrix;

uniform vec4 color;
uniform vec4 light;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    float intensity = dot(model * normal, normalize(light - pos));
    intensity = intensity > 0.95 ? 1 : (intensity > 0.7 ? 0.7 : (intensity > 0.4 ? 0.4 : (intensity > 0.1 ? 0.1 : 0.05)));

    gl_Position = projectionMatrix * view * model * pos;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
}
"""


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