
from typing import Iterable, List, Tuple, Union
import cv2
import matplotlib.pyplot as plt
import re
import numpy as np
from xml.dom import minidom as md
from queue import Queue
import warnings

def look_shape(a : Iterable) -> Tuple:
    # for debug
    return np.array(a).shape

def length_within_points(a : Iterable, empty_value : Union[int, float] = 0) -> int:
    """
        a simple instance:
            array : [empty_value, empty_value, empty_value, 1, empty_value, 0, 1, 2, empty_value]
            Then length_within_points(array) will return index diff between 1 and 2, which is 5
    """
    a = list(a)
    l_pivot, r_pivot = -1, -2
    for index, (l_val, r_val) in enumerate(zip(a[::1], a[::-1])):
        if l_val != empty_value and l_pivot == -1:
            l_pivot = index 
        if r_val != empty_value and r_pivot == -2:
            r_pivot = len(a) - index

    return r_pivot - l_pivot + 1

def dump_rings_from_image(image : np.ndarray, output_path : str, plot_dict : dict = {"color" : "k", "linewidth" : 2.0}, default_height : float = 8) -> List[np.ndarray]:
    # regular operation, no more explainations
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
    edge = cv2.Canny(gray, 50, 150)
    edge = cv2.GaussianBlur(edge,(3,3),0)
    
    # get ratio between width and height to adjust the final output
    valid_width = length_within_points(edge.sum(axis=0))
    valid_height = length_within_points(edge.sum(axis=1))
    true_ratio = valid_width / valid_height

    # get contour of the edge image
    contour_tuple = cv2.findContours(edge, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    contours = contour_tuple[0]
    rings = [np.array(c).reshape([-1, 2]) for c in contours]

    # adjust coordinate system to the image coordinate system
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for ring in rings:
        max_x = max(max_x, ring.max(axis=0)[0])
        max_y = max(max_y, ring.max(axis=0)[1])
        min_x = max(min_x, ring.min(axis=0)[0])
        min_y = max(min_y, ring.min(axis=0)[1])
    
    # adjust ratio
    plt.figure(figsize=[default_height * true_ratio, default_height])

    # plot to the matplotlib
    for _, ring in enumerate(rings):
        close_ring = np.vstack((ring, ring[0]))
        xx = close_ring[..., 0]
        yy = max_y - close_ring[..., 1]
        plt.plot(xx, yy, **plot_dict)

    plt.axis("off")
    plt.savefig(output_path)

def remove_matplotlib_background(svg_file : str, bg_node_name : str = "patch_1") -> None:
    dom_tree : md.Document = md.parse(svg_file)
    svg_node = None 
    # select the svg tag
    for node in dom_tree.childNodes:
        if node.nodeName == "svg":
            svg_node : md.Element = node 
    if svg_node is None:
        raise ValueError("not find a svg node in {}".format(svg_file))

    # bfs svg node to find the background node
    q = Queue()
    q.put(svg_node)
    target_node = None  # we will remove the target node

    while not q.empty():
        cur : md.Node = q.get()
        if cur.hasChildNodes():
            for node in cur.childNodes:
                q.put(node)
        if hasattr(cur, "getAttribute"):
            # this is the id of the background node
            if cur.getAttribute("id") == bg_node_name:
                target_node = cur
    
    if target_node is None:
        warnings.warn("background node is not found, please ensure whether bg_node_name is correct")
    else:       # remove and write
        target_node.parentNode.removeChild(target_node)
        with open(svg_file, "w", encoding="utf-8") as fp:
            dom_tree.writexml(
                writer=fp,
                indent="\t"
            )

def bitmap_to_contour_svg(input_bitmap_path : str, output_svg_path : str):
    image = cv2.imread(input_bitmap_path)
    dump_rings_from_image(image, output_path=output_svg_path)
    remove_matplotlib_background(output_svg_path)
        
def writeFile(imageName,fileName):
    f = open(fileName,'w')
    imageFile = open(imageName,'r')
    content = imageFile.readlines()
    for data in content:
        information = re.search(r'd="(.*)" style',data)
        if information:
            f.write(information.group(1)+'\n')
    f.close()
    imageFile.close()
    print(f"{fileName} has been successfully created by {imageName}")
# if __name__ == '__main__':
#     bitmap_to_contour_svg(
#         input_bitmap_path="./123.jpg",
#         output_svg_path="./images/123.svg"
#     )