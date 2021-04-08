# Shoe Store API

As backend developers, we arguably spend just as much time focusing on services and endpoints than front-facing
rendering. APIs in Python are equally easy to set up in micro-frameworks or full-scale frameworks, but using Django
allows us the use of some packages to help make our lives easier.

<span>Django REST framework</span>, a third-party package, allows us to turn Django into a full-featured REST (
Representational State Transfer) API. This is important because it gives us access to two specific benefits:

1) it allows us to use the Django ORM and all the niceties that come along with that, and

2) it's ridiculously easy to maintain both an API _and_ a front end in the same application.

There are two main concepts that this introduces: the first is a serializer, and the second is viewsets. When we work
with the models, we use the model instances (objects) to access attributes directly and interact with them. Because an
API doesn't have views in the traditional sense, we need a way to translate the model instances into a JSON format so
that it can be easily parsed and controlled. The serializers handle the transformation from model instances to the
views, then the class-based viewsets handle the formatting of the serialized data into a HTTP-compatible response. All
of the ModelViewSet classes implicitly allow GET requests, but you can do more by subclassing the "create" function and
checking out the "@action" decorator.

#### Models

* **Manufacturer**
    * name: str
    * website: url
* **ShoeType**
    * style: str
* **ShoeColor**
    * color_name: str (ROYGBIV + white / black) --> _
* **Shoe**
    * size: int
    * brand name: str
    * manufacturer: FK (<span>Foreign Key</span>)
    * color: FK
    * material: str
    * shoe_type: FK
    * fasten_type: str